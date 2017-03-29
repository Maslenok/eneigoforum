from django.contrib import admin
from django.http import HttpResponseRedirect
from energotechnology.models import  EnergotechnologySun, EnergotechnologyEast, \
    EnergotechnologyWater, EnergotechnologyOsveshenie, EnergotechnologyOtoplenie, EnergotechnologyAll


class EnergotechnologyAdmin(admin.ModelAdmin):
    view_on_site=False

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



# список приложений верхнего уровня в админке, сначало идут они , потом с отступом остальные
spisoc=[
    EnergotechnologyAll,
       ]


admin.site.register(EnergotechnologyAll, EnergotechnologyAdmin)
admin.site.register(EnergotechnologySun, EnergotechnologyAdmin)
admin.site.register(EnergotechnologyEast, EnergotechnologyAdmin)
admin.site.register(EnergotechnologyWater, EnergotechnologyAdmin)
admin.site.register(EnergotechnologyOsveshenie, EnergotechnologyAdmin)
admin.site.register(EnergotechnologyOtoplenie, EnergotechnologyAdmin)

# Register your models here.
