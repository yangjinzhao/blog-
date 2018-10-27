from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import *
from articles.forms import ArticleInfoForm
from users.models import *
def article_detail(request,articleid):
    article=ArticleInfo.objects.get(pk=articleid)
    article.click_num+=1
    article.save()#点击量增加
    articles=ArticleInfo.objects.all()
    click_order = articles.order_by('-click_num')[:5]
    addtime_order = articles.order_by('-add_time')[:5]
    love_order = articles.order_by('-love_num')[:5]
    categorys = Category.objects.all()
    all_tag = TagInfo.objects.all()
    return render(request,'article_detail.html',{'click_order':click_order,'addtime_order':addtime_order,
                                                 'love_order':love_order,'categorys':categorys,
                                                 'all_tag':all_tag,
                                                 'article': article
                                        })

def add_comment(request,articleid):
    if articleid:
        article=ArticleInfo.objects.get(pk=articleid)
        content=request.POST.get('comment')
        if content:
            if request.user.is_authenticated:
                comment_obj = CommentInfo()
                comment_obj.comment_content=content
                comment_obj.comment_person=request.user
                comment_obj.comment_article=article
                comment_obj.save()
                article.comment_num +=1
                article.save()
                return redirect(reverse('articles:article_detail',args=[articleid]))
            else:
                return HttpResponse('请您先登录')
        else:
            pass

def add_love(request):
    #articleid= request.GET.get('articleid')
    articleid = request.POST.get('articleid')
    if articleid:
        article_obj= ArticleInfo.objects.get(pk=articleid)
        article_obj.love_num+=1
        article_obj.save()
        return JsonResponse({'status':'ok','msg':'点赞成功'})
    else:
        return JsonResponse({'status':'fail','msg':'点赞失败'})


def add_article(request):
    if request.method=='GET':
        article_form = ArticleInfoForm()
        return render(request,'add_article.html',{ 'article_form': article_form})
    else:
        article_form=ArticleInfoForm(request.POST,request.FILES)
        if article_form.is_valid():
           datas= article_form.cleaned_data
           articleinfo = ArticleInfo()
           articleinfo.title = datas['title']
           articleinfo.desc = datas['desc']
           articleinfo.content = datas['content']
           articleinfo.image = datas['image']
           category=Category.objects.get(pk=datas['category'])
           articleinfo.category=category
           articleinfo.author=request.user
           articleinfo.save()
           return redirect(reverse('index'))

        return render(request,'add_article.html',{'article_form':article_form})







