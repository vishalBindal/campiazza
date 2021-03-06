# Generated by Django 2.1.7 on 2019-03-06 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Keep the name less than 50 characters', max_length=50)),
                ('price', models.PositiveIntegerField(help_text='A reasonable price (in rupees)')),
                ('description', models.TextField(max_length=1000)),
                ('category', models.CharField(choices=[('bk', 'Books'), ('el', 'electronics( smartphones and laptops ) '), ('ac', 'electronic accessories'), ('cy', 'cycles'), ('sp', 'sports'), ('ot', 'others')], default='bk', max_length=2)),
                ('condition', models.CharField(max_length=50)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemHigh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.CharField(max_length=500)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
