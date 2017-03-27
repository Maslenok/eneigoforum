from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from energoforum.settings import BASE_DIR
from energotechnology.models import  EnergotechnologySun, EnergotechnologyEast, \
    EnergotechnologyWater, EnergotechnologyOsveshenie, EnergotechnologyOtoplenie




class EnergotechnologySunAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи

        return self.model.objects.all().count() < 1


    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")


class EnergotechnologyEastAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

class EnergotechnologyWaterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")




class EnergotechnologyOsveshenieAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect("/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect("/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect("/admin/")

class EnergotechnologyOtoplenieAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(BASE_DIR+"/admin/")

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(BASE_DIR+"/admin/")

    def response_change(self, request, obj):
        return HttpResponseRedirect(BASE_DIR+"/admin/")

admin.site.register(EnergotechnologySun, EnergotechnologySunAdmin)
admin.site.register(EnergotechnologyEast, EnergotechnologyEastAdmin)
admin.site.register(EnergotechnologyWater, EnergotechnologyWaterAdmin)
admin.site.register(EnergotechnologyOsveshenie, EnergotechnologyOsveshenieAdmin)
admin.site.register(EnergotechnologyOtoplenie, EnergotechnologyOtoplenieAdmin)

# Register your models here.
