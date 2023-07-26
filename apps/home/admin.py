from django.contrib import admin
from django.utils.html import format_html
from .models import Home

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", 'imagem_tag')
    list_display_links = ("titulo", )
    list_filter = ('titulo',)
    search_fields = ('titulo',)

    def imagem_tag(self, obj):
        try:
            return format_html(f"<img src='{obj.imagem.url}' width='50' heigth='50' />")
        except:
            return ""
    imagem_tag.short_description = 'Imagens'

admin.site.register(Home, HomeAdmin)