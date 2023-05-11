from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'image', 'content', 'created_at', 'view_content', 'writer',)
    #list_editable = ('content',)
    list_filter = ('created_at',)
    search_fields = ('id', 'writer__username',)
    readonly_fields = ('created_at',)
    inlines = [CommentInline]

    actions = ['make_published']

    def make_published(modeladmin, request, querySet):
        for item in querySet:
            item.content='운영 규정 위반으로 인한 게시글 삭제처리'
            item.save()
    
    
#admin.site.register(Comment)