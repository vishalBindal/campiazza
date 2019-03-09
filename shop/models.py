from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
import datetime



class Item(models.Model):
    name = models.CharField(max_length=50, help_text='Keep the name less than 50 characters')
    price = models.PositiveIntegerField(help_text='A reasonable price (in rupees)')
    description = models.TextField(max_length=1000)

    # highlights added via ItemHigh
    category = models.CharField(
        max_length=2,
        choices=(
            ('bk', 'Books'),
            ('el', 'electronics( smartphones and laptops ) '),
            ('ac', 'electronic accessories'),
            ('cy', 'cycles'),
            ('sp', 'sports'),
            ('ot', 'others'),
        ),
        default='bk'
    )
    # images added via ItemImage
    condition = models.CharField(max_length=50,
                                 help_text="Brief statement of present condition, less than 50 characters")
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_id = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    buy_time=models.DateTimeField(blank=True, null=True)
    buyer_username = models.CharField(blank=True,null=True,max_length=100)
    buyer_address=models.CharField(blank=True,null=True,max_length=1000)
    created_datetime = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "{n} ( sold by {u} )" .format(n=self.name, u=self.seller.username)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.pk})


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prev_login = models.DateTimeField(blank=True,null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True)
    profile_pic = models.ImageField(default='avatar.jpg')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)

