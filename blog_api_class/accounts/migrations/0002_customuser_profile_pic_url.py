# Generated by Django 4.0.3 on 2022-03-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
