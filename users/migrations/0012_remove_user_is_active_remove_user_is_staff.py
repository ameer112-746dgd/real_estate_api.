# Generated by Django 5.1.1 on 2024-10-15 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_is_active_user_is_staff_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
