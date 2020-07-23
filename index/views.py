from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html',locals())
from django.http import HttpResponse
def test_view(requset):
    print('test_view被调用')
    return HttpResponse('请求到达了test页面')

import os
from django.conf import settings
def upload_view(request):
    if request.method=='GET':
        return render(request,'upload.html')
    elif request.method=='POST':
        a_file=request.FILES['myfile']
        print(a_file)
        # 计算保存文件的位置
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb')as fw:
            fw.write(a_file.file.read())
            return HttpResponse('success to upload')
        return HttpResponse('文件上传失败')