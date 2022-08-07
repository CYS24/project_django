from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Address, Brd, Member

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def list(request):
    template = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses':addresses,
    }
    return HttpResponse(template.render(context, request))

def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({},request))

from django.urls import reverse
from django.utils import timezone
def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x,addr=y,rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(requset, id):
    address = Address.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect(reverse('list'))

def update(requset, id):
    template = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address':address,
    }
    return HttpResponse(template.render(context, requset))

def update_ok(requset, id):
    x=requset.POST['name']
    y=requset.POST['addr']
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address.rdate = nowDatetime
    address.save()
    return HttpResponseRedirect(reverse('list'))

def blist(request):
    template = loader.get_template('blist.html')
    brds =  Brd.objects.all().values()
    context = {
        'brds': brds, 
    }
    return HttpResponse(template.render(context, request))

def bwrite(request):
    template = loader.get_template('bwrite.html')
    return HttpResponse(template.render({}, request))

def bwrite_ok(request):
    a = request.POST['writer']
    b = request.POST['email']
    c = request.POST['subject']
    d = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    brd = Brd(writer=a, email=b, subject=c, content=d, wdate=nowDatetime)
    brd.save()
    return HttpResponseRedirect(reverse('blist'))

def bcontent(request, id):
    template = loader.get_template('bcontent.html')
    brd =  Brd.objects.get(id=id)
    context = {
        'brd': brd, 
    }
    return HttpResponse(template.render(context, request))

def bupdate(request, id):
    template = loader.get_template('bupdate.html')
    brd = Brd.objects.get(id=id)
    context = {
        'brd': brd, 
    }
    return HttpResponse(template.render(context, request))

def bupdate_ok(request, id):
    a = request.POST['writer']
    b = request.POST['email']
    c = request.POST['subject']
    d = request.POST['content']
    brd = Brd.objects.get(id=id)
    brd.writer = a
    brd.email = b
    brd.subject = c
    brd.content = d
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    brd.wdate = nowDatetime
    brd.save()
    return HttpResponseRedirect(reverse('blist'))

def bdelete(request, id):
    brd = Brd.objects.get(id=id)
    brd.delete()
    return HttpResponseRedirect(reverse('blist'))

def login(request):
    return render(request, 'login.html')

def login_ok(request):
    email = request.POST.get('email', None)
    pwd = request.POST.get('pwd', None)
    result = 0
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        member = None
    if member != None:
        if member.pwd == pwd:
            result=2
            request.session['user'] = member.email
        else:
            result=1
    else:
        result=0
        
    template = loader.get_template('login_ok.html')
    context = {
        'result' : result,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('user'):
        request.session.clear()
    return redirect('../')
#############################################################
def test1(request):
    addresses = Address.objects.all().values()
    template = loader.get_template('template1.html')
    name = 'sana'    
    context = {
        'name' : name,
        'addresses' : addresses
    }
    return HttpResponse(template.render(context, request))

def test2(request):
    template = loader.get_template('template2.html')
    context = {
        'x' : 2,
        'y' : 'brown',
        'fruits' : ['pear', 'mango'],
        'z' : 2,
        'fruits2' : ['pear', 'mango'],
    }
    return HttpResponse(template.render(context, request))

def test3(request):
    addresses = Address.objects.all().values()
    template = loader.get_template('template3.html')
    context = {
        'fruits' : ['pear', 'mango', 'apple', 'grape'],
        'cars': [{'brand':'현대', 'model':'소나타', 'year':'2022'}, {'brand':'테슬라', 'model':'모델X', 'year':'2020'},
                 {'brand':'기아', 'model':'텔루라이드', 'year':'2021'}],
        'addresses' : addresses,
    }
    return HttpResponse(template.render(context, request))

def test4(request):
    template = loader.get_template('template4.html')
    context = {        
        'addr' : 'newyork',
    }
    return HttpResponse(template.render(context, request))

def test5(request):
    addresses = Address.objects.all().values()
    template = loader.get_template('template5.html')
    context = {        
        'addresses' : addresses,
    }
    return HttpResponse(template.render(context, request))

def test6(request):
    addresses = Address.objects.all().values()
    template = loader.get_template('template6.html')
    context = {        
        'addresses' : addresses,
    }
    return HttpResponse(template.render(context, request))

def test7(request):
    template = loader.get_template('template7.html')
    context = {}
    return HttpResponse(template.render(context, request))

def test8(request):
    template = loader.get_template('template8.html')
    context = {}
    return HttpResponse(template.render(context, request))