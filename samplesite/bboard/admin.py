from django.contrib import admin

from bboard.models import Bb
from bboard.models import Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', "rubric")
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('published', "rubric")




admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)