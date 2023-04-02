from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Name', max_length=200)
    url = models.CharField('Url', max_length=300)
    position = models.PositiveIntegerField('Position', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class MenuItem(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField('Url', max_length=255)
    position = models.PositiveIntegerField('Position', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
