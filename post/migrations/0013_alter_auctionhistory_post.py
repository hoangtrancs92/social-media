# Generated by Django 4.1.3 on 2023-04-18 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionhistory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_histories', to='post.post'),
        ),
    ]
