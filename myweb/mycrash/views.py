# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponseRedirect,render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from mycrash.models import Accident,Photo,VehicleData,PersonData
from mycrash import forms


# Create your views here.
def crashdatapage(request):
    template=get_template('index.html')
    elements=Accident.objects.all()
    # html=template.render(locals())
    request_context=RequestContext(request).push(locals())
    html=template.render(request_context)
    return HttpResponse(html)

def showelement(request,id):
    try:
        element = Accident.objects.get(id=id)
        vehicle=VehicleData.objects.filter(id=id)
        images=Photo.objects.filter(element=element)
    except:
        pass
    template=get_template('element.html')
    # html = template.render(locals())
    request_context=RequestContext(request).push(locals())
    html=template.render(request_context)
    return HttpResponse(html)
    # return render(request,"element.html",request_context)

def elementpage(request):
    if request.method=='POST':
        element_page=forms.ElementForm(request.POST)
        if element_page.is_valid():
            message="存储成功！"
            temp=element_page.save(commit=False)#commit=False时，不会真正更新数据库
            temp.NAME=temp.CITY+' '+temp.NUM#直接修改返回的模型对象内的数值
            temp.save()
            return HttpResponseRedirect("/epage")
        else:
            message="每一项都必须填，并请检查数据格式是否正确！"
    else:
        element_page = forms.ElementForm()
        message = '请输入所有的的信息再点击保存'

    # template=get_template('epage.html')
    request_context=RequestContext(request).push(locals())
    # html=template.render(request_context)
    # return HttpResponse(html)
    # return render_to_response('epage.html',request_context)
    return render(request,"epage.html",request_context)

def elementpagevehicle(request):
    if request.method=='POST':
        element_page_vehicle=forms.VehicleForm(request.POST)
        if element_page_vehicle.is_valid():
            message="车辆信息存储成功！"
            temp=element_page_vehicle.save(commit=False)#commit=False时，不会真正更新数据库
                                                        # 先将返回的模板存入一个中间变量temp中
            temp.NAME=str(temp.accident)+' V'+temp.VEH_NO#直接修改返回的模型对象内的数值
                                                        # accident是作为vehicle的primarykey，accident也是accident数据表单的名字
                                                        #！！！！！注意：一定要格式相同才能相加！！！！！
            temp.save()
            return HttpResponseRedirect("/epage/vehicle")
        else:
            message="每一项都必须填，并请检查数据格式是否正确！"
    else:
        element_page_vehicle=forms.VehicleForm
        message="请录入所有的信息再点击保存"

    request_context=RequestContext(request).push(locals())
    return  render(request,"epage_vehicle.html",request_context)

def elementpageperson(request):
    if request.method=='POST':
        element_page_person=forms.PersonForm(request.POST)
        if element_page_person.is_valid():
            message="人员信息存储成功！"
            temp=element_page_person.save(commit=False)
            temp.NAME=str(temp.vehicle)+' P'+temp.PER_NO
            temp.save()
            return HttpResponseRedirect("/epage/person")
        else:
            message="每一项都必须填，并请检查数据格式是否正确！"
    else:
        element_page_person=forms.PersonForm
        message="请录入所有信息在保存"

    request_context=RequestContext(request).push(locals())
    return render(request,"epage_person.html",request_context)

def elementpagephoto(request):
    if request.method=='POST':
        element_page_photo=forms.PhotoForm(request.POST)
        if element_page_photo.is_valid():
            message="人员信息存储成功！"
            temp=element_page_photo.save(commit=False)
            temp.NAME=str(temp.accident)+'的现场照片'
            temp.save()
            return HttpResponseRedirect('/epage/photo')
        else:
            message="每一项都必须填，并请检查数据格式是否正确！"
    else:
        element_page_photo=forms.PhotoForm
        message="请录入所有信息在保存"

    request_context=RequestContext(request).push(locals())
    return render(request,"epage_photo.html",request_context)
