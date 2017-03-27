from audioop import reverse

from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.checks import messages
from django.db import models
from ckeditor.fields import RichTextField
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import SimpleTemplateResponse
from django.utils.text import slugify
from factory.compat import force_text
from unidecode import unidecode

from staticpages.models import EnergotechnologyAll




class EnergotechnologySun(models.Model):
    class Meta:
        db_table="energotechnologysun"
        verbose_name = "Солнце"
        verbose_name_plural = "Солнце"

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)
    key=models.ForeignKey(EnergotechnologyAll, on_delete=models.CASCADE, verbose_name="Энерготехнологии")

    def save(self):
        print(" Печать self", self)
        super(EnergotechnologySun, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologySun, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class EnergotechnologyWater(models.Model):
    class Meta:
        db_table="energotechnologywater"
        verbose_name = "Вода"
        verbose_name_plural = "Вода"
    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)
    key = models.ForeignKey(EnergotechnologyAll, on_delete=models.CASCADE, verbose_name="Энерготехнологии")

    def save(self):
        super(EnergotechnologyWater, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyWater, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title





class EnergotechnologyEast(models.Model):
    class Meta:
        db_table="energotechnologyeast"
        verbose_name = "Земля"
        verbose_name_plural = "Земля"
    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)
    key = models.ForeignKey(EnergotechnologyAll, on_delete=models.CASCADE, verbose_name="Энерготехнологии")

    def save(self):
        super(EnergotechnologyEast, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyEast, self).save()

    #def delete(self, using=None, keep_parents=False):
     #   super(EnergotechnologyEast, self).delete()
      #  print("Удаление")
      #  return redirect("/")



    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class EnergotechnologyOsveshenie(models.Model):
    class Meta:
        db_table="energotechnologyosveshenie"
        verbose_name = "Освещение"
        verbose_name_plural = "Освещение"

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)
    key = models.ForeignKey(EnergotechnologyAll, on_delete=models.CASCADE, verbose_name="Энерготехнологии")


    def save(self):
        super(EnergotechnologyOsveshenie, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyOsveshenie, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class EnergotechnologyOtoplenie(models.Model):
    class Meta:
        db_table="energotechnologyotoplenie"
        verbose_name = "Отопление"
        verbose_name_plural = "Отопление"

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)
    key = models.ForeignKey(EnergotechnologyAll, on_delete=models.CASCADE, verbose_name="Энерготехнологии")

    def save(self):
        super(EnergotechnologyOtoplenie, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyOtoplenie, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

# Create your models here.
