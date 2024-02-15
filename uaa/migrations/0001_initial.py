# Generated by Django 5.0.1 on 2024-02-05 10:30

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPasswordRequestUsers',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('request_token', models.CharField(default=None, editable=False, max_length=100)),
                ('request_is_used', models.BooleanField(default=False)),
                ('request_is_active', models.BooleanField(default=True)),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'FORGOT PASSWORD REQUESTS',
                'db_table': 'ai_mpers_users_forgot_password_request',
                'ordering': ['-primary_key'],
            },
        ),
        migrations.CreateModel(
            name='UsersProfiles',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('profile_unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('profile_type', models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('DOCTOR', 'DOCTOR'), ('PHARMACIST', 'PHARMACIST'), ('PATIENTS', 'PATIENTS')], default='', max_length=100)),
                ('profile_title', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss')], default='', max_length=100)),
                ('profile_photo', models.CharField(blank=True, default='/profiles/user_profile.png', max_length=100, null=True)),
                ('profile_gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=100, null=True)),
                ('profile_has_been_verified', models.BooleanField(default=True)),
                ('profile_is_active', models.BooleanField(default=True)),
                ('profile_createddate', models.DateField(auto_now_add=True)),
                ('user_nickname', models.CharField(max_length=100, null=True, unique=True)),
                ('profile_user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'USER PROFILES',
                'db_table': 'ai_mpers_user_profiles',
                'ordering': ['-primary_key'],
            },
        ),
    ]