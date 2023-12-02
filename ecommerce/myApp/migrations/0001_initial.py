# Generated by Django 4.2.5 on 2023-11-16 10:20

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
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Marka Başlık')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori Başlık')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Renk Başlık')),
                ('color_cod', models.CharField(max_length=50, null=True, verbose_name='Renk Kodu')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('Description', models.TextField(verbose_name='Açıklama')),
                ('comments', models.IntegerField(default=0, verbose_name='Yorum Sayısı')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('image', models.ImageField(max_length=350, null=True, upload_to='product', verbose_name='Ürün Kart Resmi')),
                ('rating', models.FloatField(default=0, verbose_name='Ürün Puanı')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.brand', verbose_name='Marka')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.category', verbose_name='Kategori')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('small', 'S'), ('medium', 'M'), ('large', 'L'), ('xlarge', 'XL')], max_length=50, verbose_name='Beden')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.color', verbose_name='Renk')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.productmain', verbose_name='Ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=400, upload_to='product', verbose_name='Resim')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='myApp.productmain', verbose_name='Ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('rating', models.IntegerField(verbose_name='Yorum Puanı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.productmain', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='BasketShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.IntegerField(default=0, verbose_name='Adet')),
                ('total_price', models.FloatField(default=0, verbose_name='Toplam Fiyat')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.productinfo', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
