from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from unidecode import unidecode

from django.db import models

# Create your models here.

class MainText(models.Model):
    class Meta:
        db_table="indextText"
        verbose_name = "Информация на главной странице"
        verbose_name_plural = "Информация на главной странице"

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
        verbose_name = "Информация на на странице информации"
        verbose_name_plural = "Информация на на странице информации"

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

class FAQ(models.Model):
    class Meta:
        db_table = "faq"
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    question = models.TextField(verbose_name=u'Вопрос', )
    answer = models.TextField(verbose_name=u'Ответ', )


    def __str__(self):
        return self.question

    def __unicode__(self):
        return self.question

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


class EnergotechnologyAll(models.Model):
    class Meta:
        db_table="energotechnologyall"
        verbose_name = "Общая информация"
        verbose_name_plural = "Общая информация"

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)

    def save(self):
        super(EnergotechnologyAll, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyAll, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class EnergotechnologySun(models.Model):
    class Meta:
        db_table="energotechnologysun"
        verbose_name = "Солнце"
        verbose_name_plural = "Солнце"

    text = RichTextField(verbose_name=u'Текст', blank=True)
    title = models.CharField(max_length=100,  blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Короткое имя', blank=True)

    def save(self):
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

    def save(self):
        super(EnergotechnologyEast, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyEast, self).save()

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

    def save(self):
        super(EnergotechnologyOtoplenie, self).save()
        self.slug = slugify(unidecode(self.title))
        super(EnergotechnologyOtoplenie, self).save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title