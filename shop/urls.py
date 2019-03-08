from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('items/add/', views.itemCreate, name='item_create'),
    path('items/add/image/<int:item_id>', views.image_add, name='image_add'),
    path('register/',views.UserFormView.as_view(), name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/',views.Logout, name='logout'),
    path('profile/<int:id>',views.profile_view, name='profile'),
    path('profile/edit',views.user_edit, name='user_edit'),
    path('profile/edit/details',views.profile_edit, name='profile_edit'),
    path('search', views.search, name='search'),
    path('buy/<int:item_id>',views.buy, name='buy'),
    path('confirm/<int:item_id>',views.confirm,name='confirm'),
    path('filter', views.filter_category, name='filter')
]
