from unidecode import unidecode
from django.db import models
import ckeditor
from ckeditor.fields import RichTextField
from django.utils.text import slugify
#from django.conf import settings
#from imagekit import .all()
#from pilkit.processors import SmartResize

class Question(models.Model):
    class Meta:
        db_table="question"
        verbose_name ="Вопрос"
        verbose_name_plural = "Вопросы"

    textQuestion=models.CharField("Вопрос", max_length=255)
    dateQuestion=models.DateField(verbose_name="Дата создания вопроса", auto_now_add=True)
    usersAnswers=models.SmallIntegerField("Количество проголосовавших",blank=True,default=0)
    #requestSession=models.CharField("Сесия " , max_length=150)

    def __str__(self):
        return self.textQuestion

    def __unicode__(self):
        return self.textQuestion

class Answer(models.Model):
    class Meta:
        db_table="answer"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    textAnswer=models.CharField("Ответ", max_length=100)
    question=models.ForeignKey(Question,on_delete=models.CASCADE, verbose_name= "Относится к вопросу" )
    valueAnswer=models.SmallIntegerField("количество ответов",blank=True,default=0)



    def __str__(self):
        return self.textAnswer


    def __unicode__(self):
        return self.textAnswer


class News(models.Model):
    class Meta:
        db_table="news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    dateTime=models.DateField(verbose_name="Время создания", auto_now_add=True)
    title=models.CharField("заголовок новости",max_length=50)
    textNews=ckeditor.fields.RichTextField(verbose_name=u'Текст Новости')
    imgNews=models.ImageField(verbose_name=u'Картинка', null=True, blank=True,default='/img/noimage.jpg')
   # imgNews_resize = ImageSpecField(
   #     [SmartResize(*settings.PHOTO_IMAGE_NEWS_SMOL_SIZE)], source='news', format='JPEG', options={'quality': 94}
  #  )

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title

class Testimonials(models.Model):
    class Meta:
        db_table="testimonials"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    name=models.CharField("Имя",max_length=100)
    email=models.EmailField()
    rating=models.SmallIntegerField(verbose_name="Рейтинг")
    comment=models.TextField("Отзыв")
    dateCreate=models.DateField("Дата создания отзыва", auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class MainText(models.Model):
    class Meta:
        db_table="indextText"
        verbose_name = "Информация на главной странице"
        verbose_name_plural = "Информация на главной странице"

    mainText = ckeditor.fields.RichTextField(verbose_name=u'Текст',blank=True)
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

# Create your models here.
