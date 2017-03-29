from django.db import models
from ckeditor.fields import RichTextField



class Energotechnology(models.Model):
    class Meta:
        abstract = True

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField("Титул",max_length=100,  blank=True)

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title


class EnergotechnologyAll(Energotechnology):
    class Meta:
        db_table="energotechnologyall"
        verbose_name = "Энерготехнологии"
        verbose_name_plural = "Энерготехнологии"


class EnergotechnologySun(Energotechnology):
    class Meta:
        db_table="energotechnologysun"
        verbose_name = "Солнце"
        verbose_name_plural = "Солнце"


class EnergotechnologyWater(Energotechnology):
    class Meta:
        db_table="energotechnologywater"
        verbose_name = "Вода"
        verbose_name_plural = "Вода"


class EnergotechnologyEast(Energotechnology):
    class Meta:
        db_table="energotechnologyeast"
        verbose_name = "Земля"
        verbose_name_plural = "Земля"


class EnergotechnologyOsveshenie(Energotechnology):
    class Meta:
        db_table="energotechnologyosveshenie"
        verbose_name = "Освещение"
        verbose_name_plural = "Освещение"


class EnergotechnologyOtoplenie(Energotechnology):
    class Meta:
        db_table="energotechnologyotoplenie"
        verbose_name = "Отопление"
        verbose_name_plural = "Отопление"


# Create your models here.
