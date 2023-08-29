#from django.db import models
#from django.contrib.auth import get_user_model
#from django.core.exceptions import ValidationError
#
#User = get_user_model()
#
##def validate_event_username(username):
##    username_check = User.objects.filter(username = username)
##    if username_check.count():
##        raise ValidationError("Логин уже занят")
#
#class User_Auth(models.Model):
#    username = models.CharField("Псевдоним", max_length=64, null=True)
#    name = models.CharField("Имя", max_length=64)
#    surname = models.CharField("Фамилия", max_length=64)
#    password1 = models.DecimalField("Пароль", max_length=64)
#    password2 = models.DecimalField("Потверждение пароля", max_length=64)
#    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True, blank=True)