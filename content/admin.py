from django.contrib import admin
from .models import Answer, Question, News, Testimonials, MainText

admin.site.register(Answer, admin.ModelAdmin)
admin.site.register(Question, admin.ModelAdmin)
admin.site.register(News, admin.ModelAdmin)
admin.site.register(Testimonials, admin.ModelAdmin)
admin.site.register(MainText, admin.ModelAdmin)
# Register your models here.
