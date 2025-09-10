from modeltranslation.translator import register, TranslationOptions
from apps.blogs.models import BlogModel, BlogTagModel, BlogAuthorModel, BlogCategoryModel

@register(BlogModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content1')

@register(BlogTagModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(BlogAuthorModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('full_name','bio')

@register(BlogCategoryModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)
