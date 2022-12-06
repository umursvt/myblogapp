from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ("baslik","tarih","aktif","slug",)
    list_editable = ("aktif",)
    search_fields = ("baslik","tarih",)
    readonly_fields = ("slug",)


# Register your models here.
admin.site.register(Kripto, BlogAdmin)
admin.site.register(Yazilim, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Matematik, BlogAdmin)