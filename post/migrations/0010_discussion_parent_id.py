# Generated by Django 4.1.3 on 2023-03-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_notification_discussion_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
