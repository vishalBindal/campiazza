from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .models import Item, ItemImage, Profile
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm, LoginForm,ImageForm,ItemForm, EditUserForm, EditProfileForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, Http404
import datetime


def main(request):
    items = Item.objects.all()
    return render(request, 'main.html', {'items': items, 'request':request,'ItemImage':ItemImage})


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    count = ItemImage.objects.filter(item=item).count()
    return render(request, 'details.html', {'item': item, 'range': range(count), 'count':count})


def itemCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        item_obj=form.save(commit=False)
        item_obj.seller=request.user
        item_obj.save()
        return redirect('image_add',item_id=item_obj.pk)
    return render(request, 'Item/item_form.html', {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'User/register_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('main')

        return render(request, self.template_name, {'form': form})


def LoginView(request):
    form = LoginForm(request.POST or None)
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'User/login_form.html', {'form': form, 'error_message': "Invalid Login"})
        else:
            return render(request, 'User/login_form.html', {'form': form, 'error_message': "Invalid Login"})
    return render(request, 'User/login_form.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('main')


def profile_view(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    return render(request, 'User/profile_page.html', {'profile':profile, 'user_view':user, 'request':request,
                                                      'items': Item.objects.filter(buyer_id=request.user.id),
                                                      'seller_items':Item.objects.filter(seller=user)})


def image_add(request, item_id):
    item_details= Item.objects.get(pk=item_id)
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        image_obj=form.save(commit=False)
        if len(request.FILES)!=0:
            image_obj.item=item_details
            image_obj.image=request.FILES['image']
            image_obj.save()
        else:
            image_obj.image = 'media/cook.jpg'
        if 'more' in request.POST:
            return render(request, 'Item/itemimage_form.html', {'form': form, 'message': "Image added successfully!"})
        if 'exit' in request.POST:
            return redirect('detail',item_id)
    return render(request, 'Item/itemimage_form.html', {'form':form})


@login_required
def profile_edit(request):
    user_obj=request.user
    profile_obj=Profile.objects.get(user=user_obj)
    form= EditProfileForm(request.POST or None, instance=profile_obj)
    if form.is_valid():
        user_obj=form.save(commit=False)
        user_obj.save()
        if 'exit' in request.POST:
            return redirect('profile', request.user.id)
        if 'back' in request.POST:
            return redirect('user_edit')
    return render(request, 'User/edit_profile.html', {'form': form})


@login_required
def user_edit(request):
    user_obj=request.user
    form = EditUserForm(request.POST or None, instance=user_obj)
    if form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.save()
        return redirect('profile_edit')
    return render(request, 'User/edit_user.html', {'form': form, 'user':user_obj})


def search(request):
    query=request.GET.get('q')
    items=Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_results.html', {'items': items})


def filter_category(request):
    query = request.GET
    choices=['bk', 'el', 'ac', 'sp', 'cy', 'ot']
    for choice in choices:
        if choice in query:
            available = Item.objects.filter(Q(buyer_id=0) | Q(buyer_id=request.user.id) | Q(seller=request.user))
            items = available.filter(category=choice)
    return render(request, 'search_results.html', {'items': items})





@login_required()
def buy(request,item_id):
    item_to_be_sold=Item.objects.get(pk=item_id)
    if item_to_be_sold.seller.id == request.user.id or item_to_be_sold.buyer_id != 0:
        raise Http404("Invalid request")
    profile_details = Profile.objects.get(user=request.user)
    error=""
    if profile_details.address == '' :
        error="Your address is empty. Please fill your address in your profile first."
    return render(request,'buy_page.html',{'item':item_to_be_sold, 'profile':profile_details,'error':error})


@login_required()
def confirm(request,item_id):
    item_sold = Item.objects.get(pk=item_id)
    if item_sold.seller.id == request.user.id or item_sold.buyer_id != 0:
        raise Http404("Invalid request")
    profile_details = Profile.objects.get(user=request.user)
    item_sold.buyer_id = request.user.id
    item_sold.buy_time = datetime.datetime.now()
    item_sold.buyer_username=request.user.username
    item_sold.buyer_address=request.user.profile.address
    item_sold.save()
    return render(request, 'confirm.html', {'item': item_sold, 'profile': profile_details})


@login_required()
def admin(request):
    if not request.user.is_staff:
        raise Http404("You are not authorised")
    else:
        return HttpResponse("hey")









