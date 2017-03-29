from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from unidecode import unidecode
from django.db import models

# Create your models here.




class MainText(models.Model):
    class Meta:
        db_table="indextText"
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    mainText = RichTextField(verbose_name=u'Текст',blank=True)
    title = models.CharField(max_length=100, help_text="Информация на главной странице",blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)

    def save(self):
        super(MainText, self).save()
        self.slug = slugify(unidecode(self.title))
        super(MainText, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class InfoText(models.Model):
    class Meta:
        db_table = "infoText"
        verbose_name = "Информации"
        verbose_name_plural = "Информация"

    infoText = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100, help_text="Информация на на странице информации", blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)




    def save(self):
        super(InfoText, self).save()
        self.slug = slugify(unidecode(self.title))
        super(InfoText, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class Contact(models.Model):
    class Meta:
        db_table = "contact"
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    textContact = RichTextField(verbose_name=u'Наши контакты', blank=True)


    def __str__(self):
        return "Contact"

    def __unicode__(self):
        return "Contact"
# Create your models here.



