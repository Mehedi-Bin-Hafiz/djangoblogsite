# Generated by Django 2.2.1 on 2019-07-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
