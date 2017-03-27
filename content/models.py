from unidecode import unidecode
from django.db import models, connection
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from energoforum import settings
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
#from django.conf import settings
#from imagekit import .all()
#from pilkit.processors import SmartResize

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

class Question(models.Model):
    class Meta:
        db_table="question"
        verbose_name ="Голосование"
        verbose_name_plural = "Голосование"

    textQuestion=models.CharField("Вопрос", max_length=255)
    dateQuestion=models.DateField(verbose_name="Дата создания вопроса", auto_now_add=True)
    usersAnswers=models.SmallIntegerField("Количество проголосовавших",blank=True,default=0)
    is_active=models.BooleanField("Активный опрос",blank=False)

    def save(self):
        super(Question, self).save()
        if self.is_active:
            cursor=connection.cursor()
            cursor.execute("UPDATE question SET is_active=0 WHERE id!=%s",[self.id])
        super(Question, self).save()

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
    persent=models.SmallIntegerField(blank=True,default=0)



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
    textNews=RichTextField(verbose_name=u'Текст Новости')
    imgNews=models.ImageField(verbose_name=u'Картинка',upload_to='static/media/images/', null=True, blank=True, default='images/noimage.jpg')
   # imgNews_resize = ImageSpecField(
  #  [SmartResize(*settings.PHOTO_IMAGE_NEWS_SMOL_SIZE)], source='imgNews', format='JPEG', options={'quality': 94}
   # )

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title

class Testimonials(models.Model):
    class Meta:
        db_table="testimonials"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    name=models.CharField("Имя",max_length=100)
    email=models.EmailField(blank=True)
    rating=models.SmallIntegerField(verbose_name="Рейтинг")
    comment=models.TextField("Отзыв")
    dateCreate=models.DateField("Дата создания отзыва", auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

