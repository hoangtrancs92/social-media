# Generated by Django 4.1.3 on 2023-05-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
