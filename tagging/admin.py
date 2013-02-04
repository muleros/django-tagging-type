# -*- coding: utf-8 -*-

from django.contrib import admin
from tagging.models import Tag, TaggedItem, TagKind, TaggedItemKind
from tagging.forms import TagAdminForm


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)

admin.site.register(TaggedItemKind)
admin.site.register(TagKind)
