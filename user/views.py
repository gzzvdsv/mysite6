from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect
# Create your views here.
def reg_view(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(username)<6:
            username_error='用户名太短！'
            return render(request,'register.html',locals())
        if password != password2:
            password2_error = '两次密码不一致'
            return render(request, 'register.html', locals())
        if len(password) == 0:
            password_error = '请输入密码'
            return render(request, 'register.html', locals())

        try :
            url=models.User.objects.get(username=username)
            username_error = '用户名已经存在！'
            return render(request, 'register.html', locals())
        except:
            models.User.objects.create(
                username=username,
                password=password)
            resp=HttpResponse('成功添加到数据库和cookies')
            resp.set_cookie('username',username)
            resp.set_cookie('password', password)
            return resp
def get_cook(request):
    coo=request.COOKIES
    print(coo)
    name=request.COOKIES['username']
    password=request.COOKIES['password']
    try:
        models.User.objects.create(
            username=name,
            password=password)
        return HttpResponse('成功储存'+name + '  ' + password)
    except:
        return HttpResponse('default to add'+name+'  '+password)
def show_(request):
    users = models.User.objects.all()
    return render(request,'show.html',locals())

def login_view(request):
    if request.method=='GET':
        username=request.COOKIES.get('username','')
        return  render(request,'login.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='':
            username_error='用户名不能为空'
            return render(request,'login.html',locals())
        try:
            auser=models.User.objects.get(
                username=username,password=password
            )
            # 记录一个登陆状态记录在session里面
            request.session['user']=username
            resp=HttpResponseRedirect('/')
            if 'remember' in request.POST:
                resp.set_cookie('username',username)
            return resp
            # return HttpResponseRedirect('/')
            # return HttpResponse(auser)
        except:
            password_error='用户名或者密码不正确'
            return render(request,'login.html',locals())
def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return  HttpResponseRedirect('/')

def get_session(request):
    auser = models.User.objects.get(
        username=123456, password=11
    )
    return HttpResponse(auser.username,auser.id
                        # auser.password
                        )
from . import form
def reg2_view(request):
    if request.method=='GET':
         myform=form.MyRegForm()
         return render(request,'reg2.html',locals())
    elif request.method=='POST':
        myform = form.MyRegForm(request.POST)
        if myform.is_valid():
            dic=myform.cleaned_data
            username=dic['username']
            password=dic['password']
            password2=dic['password2']
            return HttpResponse(str(dic))
        else:
            return HttpResponse('表单验证失败')



     # html=myform.as_p()
     # print(html)
     # return HttpResponse(html)
