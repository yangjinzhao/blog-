from django.contrib import admin
from articles.models import ArticleInfo, Category,TagInfo,ArticleTag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title','desc','comment_num',
                    'content','click_num',
                    'love_num','add_time','author',
                    'image','category'
                   ]
class TagInfoAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['article','tag','add_time']
admin.site.register(ArticleInfo,ArticleInfoAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.register(TagInfo,TagInfoAdmin)
admin.site.register(ArticleTag,ArticleTagAdmin)
