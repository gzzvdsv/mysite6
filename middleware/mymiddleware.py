from django.utils.deprecation import MiddlewareMixin
from django.http import  HttpResponse
from django.http import  Http404
class MyMw(MiddlewareMixin):
    def process_request(self, request):
         print('middleware process_request')
         print('路由是',request.path)
         print('请求方式是',request.method)
         if request.path=='/aaaa':
             return HttpResponse('当前路由是/aaaa')


class VisitLimit(MiddlewareMixin):
    # 此字典的键位IP地址，值位访问次数
    visit_times={}
    def process_request(self,request):
        ip=request.META['REMOTE_ADDR']
        if request.path_info!='/test':
            return None
        else:
            times=self.visit_times.get(ip,0)
            print('IP',ip,'以访问过/test',times,'次')
            self.visit_times[ip]=times+1
            if times<5:
                return None
            return HttpResponse('您已经访问过'+str(times)+'次')

