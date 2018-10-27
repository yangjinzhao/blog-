#文章简介，标题  图片  类别
from django import  forms
from django.forms import fields,widgets
from articles.models import   Category
class ArticleInfoForm(forms.Form):
    title = fields.CharField(max_length=50,min_length=5,label='文章标题',error_messages={
        'max_length':'文章标题不能超过50','min_length':'文章标题不能少于5'
    })
    desc = fields.CharField(max_length=200,min_length=5,label='文章简介',error_messages={
        'max_length':'文章简介不能超过200','min_length':'文章简介不能少于5'
    })
    content= fields.CharField(widget=widgets.Textarea,label='文章内容')
    image = fields.ImageField(label='文章图片')
    category = fields.ChoiceField(label='文章类别',widget=widgets.Select,choices=[])

    def __init__(self,*args,**kwargs):
        super(ArticleInfoForm, self).__init__(*args,**kwargs)
        self.fields['category'].choices =Category.objects.all().values_list('id','name')

