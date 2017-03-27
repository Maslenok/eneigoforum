from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import MainText, InfoText, Contact, EnergotechnologyAll


class MainTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

class InfoTextAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

class EnergotechnologyAllAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")



admin.site.register(MainText, MainTextAdmin)
admin.site.register(InfoText, InfoTextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(EnergotechnologyAll, EnergotechnologyAllAdmin)

# Register your models here.
