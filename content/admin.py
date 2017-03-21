from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Answer, Question, News, Testimonials, MainText, InfoText
from django.forms import ModelForm



class AnswerInlines(admin.TabularInline):
    model = Answer
    extra = 3
    fields = ("textAnswer","valueAnswer","persent")
    readonly_fields = ("valueAnswer","persent")

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlines, ]
    fields = ("textQuestion", "is_active","dateQuestion","usersAnswers",)
    readonly_fields = ("dateQuestion","usersAnswers",)
    list_display = ("textQuestion","dateQuestion", "usersAnswers", "is_active")
    list_editable = ("is_active",)

class MainTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class InfoTextAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

#admin.site.register(Answer, admin.ModelAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(News, admin.ModelAdmin)
admin.site.register(Testimonials, admin.ModelAdmin)
admin.site.register(MainText, MainTextAdmin)
admin.site.register(InfoText, InfoTextAdmin)
# Register your models here.


