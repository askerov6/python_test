from .models import Hotel
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name_hotel', 'description', "addres", 'city', 'country')
