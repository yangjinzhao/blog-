from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.middleware.security import MiddlewareMixin

class M1(MiddlewareMixin):
    def process_request(self,request):
        addr= request.META['REMOTE_ADDR']
        addr_list =['10.0.127.213','10.0.127.11','10.0.127.44']
        if addr in addr_list:
            return HttpResponse('拒绝访问')

    def process_view(self,request,callback,call_args,call_kwargs):
        # response = callback(request)
        #
            pass
class M2(MiddlewareMixin):
    def process_request(self,request):
        if request.path.startswith('/articles/add_love'):
            if not request.user.is_authenticated:
                return JsonResponse({'status': 'fail', 'msg': 'not login'})
        if request.path.startswith('/articles/add_comment/'):
            if not request.user.is_authenticated:
                return render(request, 'user_login.html', {'msg': '请您先登录'})
    # def process_response(self,request,response):
    #     pass
    #



