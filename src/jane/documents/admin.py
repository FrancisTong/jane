# -*- coding: utf-8 -*-

from django.contrib import admin

from jane.documents import models


class ResourceTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.ResourceType, ResourceTypeAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'resource_type', 'name']
    list_filter = ['resource_type__name']

admin.site.register(models.Resource, ResourceAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'resource', 'revision', 'filename', 'filesize',
        'created_at']
    list_filter = ['resource__resource_type__name', 'created_at',
        'modified_at']
    readonly_fields = ['format_data']

admin.site.register(models.Document, DocumentAdmin)
