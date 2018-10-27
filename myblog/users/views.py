from django.shortcuts import render,redirect,reverse
from users.forms import *
from users.models import *
from django.contrib.auth import authenticate, login, logout
from articles.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):
    '''
    num_pages 总页数
    page()  获取页码的数据
    :param request:
    :return:
    '''
    articles=ArticleInfo.objects.all()
    click_order = articles.order_by('-click_num')[:5]
    addtime_order = articles.order_by('-add_time')[:5]
    love_order = articles.order_by('-love_num')[:5]
    categorys = Category.objects.all()
    all_tag = TagInfo.objects.all()
    #获取tagid
    tagid=request.GET.get('tagid','')
    if tagid:
       article_tags= ArticleTag.objects.filter(tag_id=int(tagid))
       print(article_tags)
       articles= [ article_tag.article  for  article_tag in article_tags]#这个标签所对应的对象，取这个对象所对应的所有文章
    # for category in categorys:
    #     category.articleinfo_set.count()
    category_id = request.GET.get('categoryid','')
    if category_id:
        category_obj= Category.objects.get(pk=category_id)
        articles=category_obj.articleinfo_set.all()

    #创建分页器
    paginator=Paginator(articles,5)
    #获取页码数
    page_number=request.GET.get('page','1')
    try:
        page_obj=paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj.has_previous()
    page_obj.has_next()
    return render(request,'index.html',{'articles':page_obj,'page_number':page_number,'click_order':click_order,
    'addtime_order':addtime_order,'love_order':love_order,'categorys':categorys,'all_tag':all_tag,'tagid':tagid,'categoryid':category_id,
                                        })

def user_register(request):
    if request.method=='GET':
        return render(request,'user_register.html')
    else:
        user_reform = UserRegisterForm(request.POST)
        if user_reform.is_valid():
            username = user_reform.cleaned_data['username']
            password = user_reform.cleaned_data['password']
            password1 = user_reform.cleaned_data['password1']
            user=UserProfile.objects.filter(username=username)
            if user:
                return  render(request,'user_register.html',{'msg':'用户名已被注册'})
            else:
                if password==password1:
                   userprofile= UserProfile()
                   userprofile.username=username
                   userprofile.set_password(password)
                   userprofile.save()
                   return redirect(reverse('users:user_login'))

                else:
                    return render(request, 'user_register.html', {'msg': '两次密码不一致'})



        else:
            return render(request,'user_register.html',{'user_reform':user_reform})

def user_login(request):
    if request.method=='GET':
        return  render(request,'user_login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user= authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return render(request, 'user_login.html', {'msg': '用户名或密码错误'})


        else:
            return render(request,'user_login.html',{'user_loginform':user_login_form})

def user_logout(request):
    logout(request)
    return  redirect(reverse('index'))