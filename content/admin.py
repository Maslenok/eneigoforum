from django.contrib import admin
from .models import Answer, Question, News, Testimonials, FAQ


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

class TestimonialsAdmin(admin.ModelAdmin):
    fields = ("name", "email", "rating", "comment",)
    readonly_fields = ("name", "email", "rating", "comment",)
    list_display = ("name", "email", "rating", )
    list_filter=["name", "email", "rating", ]
    list_per_page=5

    def has_add_permission(self, request):  # из админки не разрешено создавать записи
        return  False

class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",  )
    fields = ("question", "answer", )


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(News, admin.ModelAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)



