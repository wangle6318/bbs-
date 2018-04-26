from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Articles(models.Model):
    title = models.CharField('标题', max_length=300)
    author = models.ForeignKey(User, verbose_name='作者', related_name="article_posts")
    abstract = models.TextField('摘要', max_length=1000, blank=True)
    attachment = models.FileField('附件', null=True, blank=True)
    body = models.TextField('文章', null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # auto_now_add : 创建时间戳，不会被覆盖
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # auto_now: 自动将当前时间覆盖之前时间
    views = models.PositiveIntegerField('浏览量', default=0)
    collects = models.ManyToManyField(User, verbose_name='收藏人', blank=True, null=True)
    comments = models.PositiveIntegerField('评论量', default=0)
    # 目录分类
    # on_delete 当指向的表被删除时，将该项设为空
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'
        ordering = ("-created_time",)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    另外一个表,储存文章的分类信息
    文章表的外键指向
    """
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = '标签管理'

    def __str__(self):
        return self.name


class Comments(models.Model):
    artid = models.ForeignKey(Articles, verbose_name='评论文章', related_name="post_comment")
    content = models.TextField('评论内容')
    author = models.ForeignKey(User, verbose_name='作者', related_name="user_comment")
    submit_date = models.DateTimeField('评论时间', auto_now_add=True)

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = '评论管理'
        ordering = ("-submit_date",)

    def __self__(self):
        return self.content


class CommentsReply(models.Model):
    art_id = models.ForeignKey(Articles, verbose_name='回复文章', related_name="reply_article")
    comment = models.ForeignKey(Comments, verbose_name='回复评论', related_name="reply_comment", blank=True, null=True)
    content = models.TextField('回复内容')
    author_id = models.ForeignKey(User, verbose_name='作者', related_name="user_reply")
    author_to = models.ForeignKey(User, verbose_name='回复给', related_name="reply_to")
    submit_date = models.DateTimeField('评论时间', auto_now_add=True)

    class Meta:
        verbose_name = '回复管理'
        verbose_name_plural = '回复管理'
        ordering = ("submit_date",)

    def __self__(self):
        return self.content


class College(models.Model):
    name = models.CharField('学院', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '学院管理'
        verbose_name_plural = '学院管理'

    def __str__(self):
        return self.name


class PersonalInfo(models.Model):
    sex_choice = (
        (u'M', u'男'),
        (u'F', u'女'),
        (u'N', u'保密'),
    )
    user = models.OneToOneField(User, verbose_name='用户名', unique=True)
    sex = models.CharField('性别', max_length=2, choices=sex_choice, default='N')
    born = models.DateField('出生日期', default='1990-1-1')
    intro = models.TextField('个人简介', null=True, blank=True)
    college = models.ForeignKey(College, verbose_name='学院', null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '个人信息管理'
        verbose_name_plural = '个人信息管理'
        ordering = ("-created_time",)

    def __str__(self):
        return str(self.user_id)


class CarouselImg(models.Model):
    carousel = models.ImageField('轮播图', upload_to='carousel/', unique=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图管理'
        ordering = ("id",)

    def __str__(self):
        return str(self.id)