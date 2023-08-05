from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=120)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return "%s (%s, %s, %s)" % (self.__class__.__name__, f'id={self.id}', f'title={self.title}', f'price={self.price}')

    class Meta:
        db_table = "advertisements"