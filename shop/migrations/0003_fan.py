# Generated by Django 4.2.5 on 2023-11-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_switch_image_alter_switch_desc_alter_switch_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
