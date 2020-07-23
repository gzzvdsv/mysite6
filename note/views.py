from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import  HttpResponse
# Create your views here.
from user import models
from .models import Note


def check_login(fn):
    def wrap(request,*args,**kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request,*args,**kwargs)
    return wrap
def list_view(request):
    if not hasattr(request,'session'):
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    username=request.session['user']
    auser=models.User.objects.get(username=username)
    notes=Note.objects.filter(user_id=auser.id)
    return render(request,'showall.html',locals())
@check_login
def add_view(request):
    if request.method=='GET':
        return render(request,'add_note.html')
    elif request.method=='POST':
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        username=request.session['user']
        n_user=models.User.objects.get(username=username)
        anote=Note(user=n_user)
        anote.title=title
        anote.content=content
        anote.save()
        return HttpResponseRedirect('/note/')
import datetime as d
@check_login
def mod_view(request,n):

    n=n
    note = Note.objects.get(id=n)
    if request.method=='GET':
        return render(request,'mod.html',locals())
    elif request.method=='POST':
        title=request.POST.get('title','')
        if title=='':
            title=note.title
        # r= HttpResponse(title)
        content=request.POST.get('content','')
        # content+=note.content
        up_note=Note(id=n)
        up_note.create_time=note.create_time
        up_note.title=title
        up_note.content=content+note.content
        up_note.user_id=note.user_id
        up_note.mod_time=d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        up_note.save()
        return  HttpResponseRedirect('/note/')
        # return HttpResponse(content)
@check_login
def del_view(request,n):
    note=Note.objects.get(id=n)
    note_userid=note.user_id
    username = request.session['user']
    user=models.User.objects.get(username=username)
    if user.id!=note_userid:
        return HttpResponseRedirect('/user/login')
    note.delete()
    return HttpResponseRedirect('/note/')






    # user_id=(models.User(username=username)).id
    # return HttpResponse(str(user.id) + '     UUUUUUUUUUUUUUUUUUU     ' + str(note_userid))
    # if str(user_id)==str(n):
    #    return HttpResponse('del'+n)
    # else:
    #     return HttpResponse(user_id+'UUUUUUUUUUUUUUUUUUU'+n)
from django.core.paginator import  Paginator
def list2_view(request):
    if not hasattr(request,'session'):
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    username=request.session['user']
    auser=models.User.objects.get(username=username)
    notes=Note.objects.filter(user_id=auser.id)
    # 在此处添加分页功能
    paginator=Paginator(notes,5)
    print(paginator)
    cur_page=request.GET.get('page',1)
    cur_page=int(cur_page)
    page=paginator.page(cur_page)
    # print('page',page)
    return render(request,'lit_.html',locals())