
from django.contrib import admin
from .models import Contents


class ContentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'word_text', 'date_time')


admin.site.register(Contents, ContentsAdmin)
