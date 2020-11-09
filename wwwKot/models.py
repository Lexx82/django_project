from django.db import models


# Create your models here.


class WwwTbl(models.Model):
    dep = models.ForeignKey('DepTbl', on_delete=models.PROTECT)
    hw_info = models.ForeignKey('HwTbl', on_delete=models.PROTECT)
    url = models.URLField(verbose_name='Ссылка')
    note = models.TextField(blank=True, verbose_name='Заметки')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'URL адрес'
        verbose_name_plural = 'URL адреса'


class DepTbl(models.Model):
    dep = models.CharField(max_length=100, verbose_name='Расположение')

    def __str__(self):
        return self.dep

    class Meta:
        verbose_name = 'Место расположения'
        verbose_name_plural = 'Места расположения'


class HwTbl(models.Model):
    hw_info = models.CharField(max_length=100, verbose_name='Железо')

    def __str__(self):
        return self.hw_info

    class Meta:
        verbose_name = 'Железо'
        verbose_name_plural = 'Железки'

