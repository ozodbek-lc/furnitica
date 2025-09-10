from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.pages.models import ContactModel, AboutModel, AuthorModel

admin.site.register(ContactModel)

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(AboutModel)
class AboutModelAdmin(TranslationAdmin):
    list_display = ['id','title', 'author']
    search_fields = ['title', 'content']
    list_filter = ['author',]

@admin.register(AuthorModel)
class AuthorModelAdmin(TranslationAdmin):
    list_display = ['id','full_name']
    search_fields = ['full_name']
    list_filter = ['created_at']