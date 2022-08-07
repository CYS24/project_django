from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User, Worldcup

def home(request):
    template = loader.get_template('home.html')
    worldcups = Worldcup.objects.all().values()
    context = {
        'worldcups' : worldcups,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('pj_login.html')
    return HttpResponse(template.render({},request))

def login_ok(request):    
    # email = request.POST['email']
    email = request.POST.get('email',None)
    # pwd = request.POST['pwd']
    pwd = request.POST.get('pwd',None)
    try:
        login_user = User.objects.get(id=email)   # ID를 DB로부터 가져오는 과정
    except User.DoesNotExist:
        login_user = None    
    result=0    
    if login_user !=None:
        #아이디있을때        
        if login_user.pwd == pwd:
            #아디비번까지 이맞음
            result = 2            
            request.session['login_ok_user'] = login_user.id
        else:
            #아이디만 맞음
            result = 1
    else:pass            
    context={
        'result':result,
    }           
    print(result)
    # request.session.clear()
    template = loader.get_template('pj_login.html')
    return HttpResponse(template.render(context, request))
    
    # if result==2:
    #     template = loader.get_template('home.html')
    #     return HttpResponse(template.render(context, request))
    # else:
    #     template = loader.get_template('login.html')
    #     return HttpResponse(template.render(context, request))
    
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))
    
def register_ok(request):
    
    id = request.POST.get('userid',None)
    username = request.POST.get('username',None)
    pwd = request.POST.get('pwd1',None)
    print(id,username,pwd)
    try:
        signup_user = User.objects.get(id=id)   # ID를 DB로부터 가져오는 과정
    except User.DoesNotExist:
        signup_user = None
    
    result=0 #가입실패
    if signup_user==None:
        #가입신청한 아이디가 없을때 
        new_member = User(id=id, username=username, pwd=pwd)
        new_member.save()
        result=1 # 가입성공
    else:pass
    context={
        'result':result,
    }    
    
    template = loader.get_template('register.html')
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        request.session.clear()        
    return redirect("/")

def password(request):
    template = loader.get_template('password.html')
    return HttpResponse(template.render({}, request))

def modaltest(request, id):
    template = loader.get_template('modaltest.html')
    g_name = Worldcup.objects.get(id=id).g_name
    context = {
        'g_name' : g_name,
    }
    return HttpResponse(template.render(context, request))

from .models import Tables
from django.urls import reverse
from django.utils import timezone

def tables(request):
    temlate = loader.get_template('tables.html')
    tabless =  Tables.objects.all().values()
    context = {
        'tabless': tabless, 
    }
    return HttpResponse(temlate.render(context, request))

def write(request):
    temlate = loader.get_template('pj_write.html')
    return HttpResponse(temlate.render({}, request))	

def write_ok(request):
    a = request.POST['subject']
    b = request.POST['content']
    c = request.POST['name']
    d = request.POST.get('views', False)
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    table = Tables(subject=a, content=b, name=c, date=nowDatetime, views=d)
    table.save()
    return HttpResponseRedirect(reverse('tables'))

def delete(request, id):
    Table = Tables.objects.get(id=id)
    Table.delete()
    return HttpResponseRedirect(reverse('tables'))

def update(request, id):
    temlate = loader.get_template('pj_update.html')
    table = Tables.objects.get(id=id)
    context = {
        'table': table, 
    }
    return HttpResponse(temlate.render(context, request))

def update_ok(request, id):
    a = request.POST['subject']
    b = request.POST['content']
    c = request.POST['name']
    d = request.POST.get('views', False)
    Table = Tables.objects.get(id=id)
    Table.subject = a
    Table.content = b
    Table.name = c
    Table.views = d
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S') #옵션
    Table.date = nowDatetime #옵션
    Table.save()
    return HttpResponseRedirect(reverse('tables'))

def content(request, id):
    temlate = loader.get_template('content.html')
    table = Tables.objects.get(id=id)
    context = {
        'table': table, 
    }
    return HttpResponse(temlate.render(context, request))

