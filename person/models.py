from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models

from department.models import Department
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Override django user model
    """
    username = models.CharField(max_length=64, unique=True, verbose_name='Login')
    first_name = models.CharField(max_length=32, db_index=True, verbose_name='First_name')
    last_name = models.CharField(max_length=32, verbose_name='Last_name')
    middle_name = models.CharField(max_length=32, verbose_name='Middle_name')
    duty = models.CharField(max_length=64, blank=True, null=True, verbose_name='Duty')
    age = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Age')
    salary = models.FloatField(blank=True, null=True, verbose_name='Salary')
    photo = models.ImageField(upload_to='media/persons', blank=True, verbose_name='Photo')
    
    is_active = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False) 

    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='person_department', verbose_name='Department')
    
    groups = models.ManyToManyField(Group, related_name='person_groups',
                                    verbose_name='Группы', blank=True, null=True)
    
    user_permissions = models.ManyToManyField(Permission, related_name='person_perms',
                                              verbose_name='Права', blank=True, null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    @property
    def department_name(self):
        return self.department.name

    def get_full_name(self) -> str:
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.middle_name)
        return full_name.strip()