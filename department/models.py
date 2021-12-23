from django.contrib.auth import get_user_model
from django.db import models
from naimium_test.settings import AUTH_USER_MODEL as User


class Department(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Name')
    """
    During first 'makemigration department' you need comment field 'director' because of mutual connection with person model.
    After applying all initialize migrations you can uncomment field 'director' and apply 'makemigration department'
    """
    director = models.OneToOneField(User,
                                    null=True,
                                    blank=True,
                                    unique=True,
                                    on_delete=models.SET_NULL,
                                    related_name='director_department',
                                    verbose_name='Director')
    
    @property
    def count_persons(self):
        users = get_user_model().objects.filter(department=self)
        return users.count()

    @property
    def count_salary(self):
        users = get_user_model().objects.filter(department=self)
        salary = sum([user.salary for user in users])
        return salary

    @property
    def director_name(self):
        return self.director.get_full_name()
    
    def __str__(self) -> str:
        return f'Отдел "{self.name}"'