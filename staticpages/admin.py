from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import MainText, InfoText, Contact

class StaticAdmin (admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['notUrl'] = True   # запрет вывода строки пути

        return self.changeform_view(request, None, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['notUrl'] = True   # запрет вывода строки пути
        return self.changeform_view(request, object_id, form_url, extra_context)


admin.site.register(MainText, StaticAdmin)
admin.site.register(InfoText, StaticAdmin)
admin.site.register(Contact, StaticAdmin)


# Register your models here.
