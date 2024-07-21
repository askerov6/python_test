from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Hotel)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = {
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        }
        css = dict(screen=('modeltranslation/css/tabbed_translation_fields.css',))


admin.site.register(HotelImage)
admin.site.register(Room)
admin.site.register(ImageRoom)
admin.site.register(Booking)


