from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time', 'last_modified_time',)
    search_fields = ('name',)
    verbose_name = '标签管理'




class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time', 'last_modified_time',)
    search_fields = ('name',)
    verbose_name = u'学院管理'


class AricleAdmin(admin.ModelAdmin):
    list_display = ('title','author','abstract','category','attachment','views','comments','created_time','last_modified_time',)
    search_fields = ('title','author','category')
    list_filter = ('author','category',)
    list_per_page = 20
    ordering = ['created_time','last_modified_time']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('artid', 'author', 'content', 'submit_date',)
    search_fields = ('artid', 'author', 'content',)
    list_filter = ('author',)
    list_per_page = 20
    ordering = ['submit_date']


class CommentsReplyAdmin(admin.ModelAdmin):
    list_display = ('art_id','author_id','content','author_to',)
    search_fields = ('art_id','author_id','author_to','content',)
    list_filter = ('author_id','author_to',)
    list_per_page = 20
    ordering = ['submit_date']


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'intro', 'born', 'college', 'created_time', 'last_modified_time',)
    search_fields = ('user', 'intro',)
    list_filter = ('sex', 'born', 'college',)
    list_per_page = 20
    ordering = ['created_time', 'last_modified_time']


class CarouselImgAdmin(admin.ModelAdmin):
    list_display = ('id','carousel','created_time','last_modified_time',)


admin.site.site_header = '师生互动平台后台管理系统'
admin.site.site_title = '师生互动平台'
admin.site.register(Category, CategoryAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Articles, AricleAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CommentsReply, CommentsReplyAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(CarouselImg, CarouselImgAdmin)

