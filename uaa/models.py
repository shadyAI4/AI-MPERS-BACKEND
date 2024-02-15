from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid
from django.utils import timezone

from uaa.managers import UserManager
# Create your models here.
# from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
('MALE', 'MALE'),
('FEMALE', 'FEMALE'),
)

USER_PROFILES_TYPES = (
('ADMIN', 'ADMIN'),
('DOCTOR', 'DOCTOR'),
('PHARMACIST', 'PHARMACIST'),
('PATIENTS', 'PATIENTS'),
)

USER_TITLE = (
('Mr', 'Mr'),
('Mrs', 'Mrs'),
('Miss', 'Miss'),
)

class UsersProfiles(models.Model):
    primary_key = models.AutoField(primary_key=True)
    profile_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    profile_type = models.CharField(default='', choices=USER_PROFILES_TYPES, max_length=100, blank=True)
    profile_title = models.CharField(default='', max_length=100, choices = USER_TITLE, blank=True)
    profile_photo = models.CharField(default='/profiles/user_profile.png', max_length=100, blank=True , null=True)
    profile_gender = models.CharField(max_length=100 , null=True , choices=GENDER_CHOICES)
    profile_user = models.OneToOneField(User, related_name='profile_user', on_delete=models.CASCADE, blank=True)
    profile_has_been_verified = models.BooleanField(default=True)
    profile_is_active = models.BooleanField(default=True)
    profile_createddate = models.DateField(auto_now_add=True)
    user_nickname = models.CharField(max_length=100, null=True, unique =True)


    class Meta:
        db_table = 'ai_mpers_user_profiles'
        ordering = ['-primary_key']
        verbose_name_plural = "USER PROFILES"

    def __str__(self):
        return "{}-{}".format(self.profile_title, self.profile_user)




class ForgotPasswordRequestUsers(models.Model):
    primary_key = models.AutoField(primary_key=True)
    request_user = models.ForeignKey(User, related_name='request_profile', on_delete=models.CASCADE)
    request_token = models.CharField(max_length=100, editable=False, default=None)
    request_is_used = models.BooleanField(default=False)
    request_is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'ai_mpers_users_forgot_password_request'
        ordering = ['-primary_key']
        verbose_name_plural = "FORGOT PASSWORD REQUESTS"

    def __str__(self):
        return "{} - {}".format(self.request_user, self.request_token)
