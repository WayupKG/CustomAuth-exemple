from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Пользователь """
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=40, blank=True)
    first_name = models.CharField(_('Имя'), max_length=40, blank=True)
    sur_name = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    slug = models.SlugField(_("slug"))

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'last_name', 'first_name']

    class Meta:
        db_table = 'User'
        unique_together = ('username', 'email', 'phone')
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        """ Возвращает full_name """
        if self.sur_name:
            return f"{self.first_name} {self.last_name} {self.sur_name}".strip()
        return f"{self.first_name} {self.last_name}".strip()
