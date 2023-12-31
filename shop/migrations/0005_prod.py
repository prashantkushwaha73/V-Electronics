# Generated by Django 4.2.5 on 2023-11-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_led'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
                ('desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
