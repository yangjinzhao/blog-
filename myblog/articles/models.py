from datetime import datetime

from django.db import models
from users.models import *
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='文章类别')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return  self.name

    class Meta:
        verbose_name='文章分类'
        verbose_name_plural=verbose_name

class ArticleInfo(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    desc = models.CharField(max_length=200,verbose_name='文章简介')
    content = models.TextField(verbose_name='文章内容')
    comment_num = models.IntegerField(verbose_name='评论数',default=0)
    click_num = models.IntegerField(verbose_name='点击量',default=0)
    love_num = models.IntegerField(verbose_name='点赞数',default=0)
    image = models.ImageField(upload_to='article/%y/%m/%d',max_length=120,verbose_name='文章图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='文章作者')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='文章类别')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='文章信息'
        verbose_name_plural=verbose_name

class TagInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='标签添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='标签信息'
        verbose_name_plural=verbose_name

class ArticleTag(models.Model):
    article = models.ForeignKey(ArticleInfo,verbose_name='所属文章',on_delete=models.CASCADE,default=None)
    tag = models.ForeignKey(TagInfo,verbose_name='所属标签',on_delete=models.CASCADE,default=None)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间',)
    def __str__(self):
        return  self.article.title
    class Meta:
        #联合索引
        unique_together=('article','tag')
        verbose_name='文章标签信息'
        verbose_name_plural =verbose_name

  #评论表
class CommentInfo(models.Model):
    comment_person = models.ForeignKey(UserProfile,verbose_name='评论人',on_delete=models.CASCADE)
    comment_article = models.ForeignKey(ArticleInfo,verbose_name='评论文章',on_delete=models.CASCADE)
    comment_content = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='评论时间')

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name='评论信息表'
        verbose_name_plural =verbose_name
