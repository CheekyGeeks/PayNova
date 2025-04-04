# Generated by Django 4.2.7 on 2025-03-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_cvv'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='face_verification_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='face_verification_token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
