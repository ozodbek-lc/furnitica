from modeltranslation.translator import register, TranslationOptions
from apps.pages.models import AboutModel,AuthorModel

@register(AboutModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(AuthorModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','bio')