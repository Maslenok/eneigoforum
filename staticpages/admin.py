from django.contrib import admin
from .models import EnergotechnologyAll, EnergotechnologySun, EnergotechnologyEast, EnergotechnologyWater,EnergotechnologyOsveshenie, EnergotechnologyOtoplenie, \
    MainText, InfoText, Contact, FAQ


class MainTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class InfoTextAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class ContactAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1


class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",  )
    fields = ("question", "answer", )

class EnergotechnologyAllAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class EnergotechnologySunAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class EnergotechnologyEastAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class EnergotechnologyWaterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class EnergotechnologyOsveshenieAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

class EnergotechnologyOtoplenieAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):  # из админки не разрешено создавать больше одной записи
        return self.model.objects.all().count() < 1

admin.site.register(EnergotechnologyAll, EnergotechnologyAllAdmin)
admin.site.register(EnergotechnologySun, EnergotechnologySunAdmin)
admin.site.register(EnergotechnologyEast, EnergotechnologyEastAdmin)
admin.site.register(EnergotechnologyWater, EnergotechnologyWaterAdmin)
admin.site.register(EnergotechnologyOsveshenie, EnergotechnologyOsveshenieAdmin)
admin.site.register(EnergotechnologyOtoplenie, EnergotechnologyOtoplenieAdmin)
admin.site.register(MainText, MainTextAdmin)
admin.site.register(InfoText, InfoTextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(FAQ, FAQAdmin)

# Register your models here.
