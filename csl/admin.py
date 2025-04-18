from django.contrib import admin
from django import forms
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from tinymce.widgets import TinyMCE

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 100, 'rows': 30},
                mce_attrs={
                    'plugins': 'link image lists media table',
                    'toolbar': "undo redo |link image | styles | bold italic underline strikethrough | align | bullist numlist",
                    'skin': 'oxide-dark',
                    'content_css': 'dark',
                    'width': 1000,
                    'resize': True,
                    'image_advtab': True,
                }
            ))
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)