# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader,Context,Template
from django.http import HttpResponse
from .models import *
import datetime
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators import csrf

# Create your views here.

def cxym(request):
    yhid=''
    if request.POST:
        yhid= request.POST['yhid']
    yzm = YyServiceitems.objects.filter(id__ccuscode=yhid) or '未查询到结果'
    return render(request,'cxym.html',{'yzm':yzm})



def index1(req):
    t = Template('<h1>hello {{uname}}</h1>')
    c = Context({'uname':'loss'})
    return HttpResponse(t.render(c))

def index(request):
    start_date = datetime.date(2017, 8, 30)
    end_date = datetime.datetime.now()
    yyst = YyServiceitems.objects.filter(id__ddate__range=(start_date,end_date))
    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(yyst, 12, request=request)  # 获取有多少页
        article_list = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render_to_response('index.html', {'uname':article_list,'page_obj': article_list})



def tong_ji(request):
    dj_kstime = 0  #单据开始时间
    dj_jstime = 0  #单据结束时间
    yz_kstime = 0   #验证开始时间
    yz_jstime = 0   #验证结束时间
    dj_bh = 0   #单据编号
    all_orgs = YyServiceitems.objects.filter(id__ddate__range=(dj_kstime,dj_jstime),submitdate_range=(yz_kstime,yz_jstime),id__cvouchcode=dj_bh,)




