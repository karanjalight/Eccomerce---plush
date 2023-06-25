# Generated by Django 2.2.14 on 2023-06-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False, help_text='0 = default ,  1= Trending ')),
                ('description', models.TextField(max_length=400)),
                ('trending', models.BooleanField(default=False, help_text='0 = default ,  1= Trending ')),
            ],
        ),
    ]
