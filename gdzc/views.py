#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from forms import gdzcForm
# from forms import Order2StepForm, Order3StepForm
from models import gdzcinfoModel
import datetime

def about(request):
    return render_to_response('about.html')

def modify(request, curid='1'):
    result = gdzcinfoModel.objects.filter(id=curid)
    form = gdzcForm()
    if request.method == "POST":
        if request.POST['curid'] == "":
            return HttpResponseRedirect('/select/') # Redirect
        result = gdzcinfoModel.objects.get(id=request.POST['curid'])
        result.adminpp     = request.POST['adminpp']
        result.adminclass  = request.POST['adminclass']
        result.isuse       = request.POST['isuse']
        result.demo        = request.POST['demo']
        result.save()
        return HttpResponseRedirect('/select/') # Redirect

    if len(result) != 0:
        result = result[0]
        form.fields["demo"].initial = result.demo
        form.fields["adminclass"].initial = result.adminclass
        form.fields["adminpp"].initial = result.adminpp
        form.fields["isuse"].initial = result.isuse
    else:
        result = ""
    return render_to_response('modifygdzc.html', {'form':form, 'curgdzc':result})

def select(request):
    if request.method == "POST":
        form = gdzcForm(request.POST)
        yeardate    = request.POST['dateyear']
        adminclass  = request.POST['adminclass']
        isuse       = request.POST['isuse']
        adminpp     = request.POST['adminpp']

        if yeardate != "":
            result = gdzcinfoModel.objects.filter(buydate__year=yeardate, adminclass__contains=adminclass, adminpp__contains=adminpp, isuse__contains=isuse)
        else:
            result = gdzcinfoModel.objects.filter(adminclass__contains=adminclass, adminpp__contains=adminpp, isuse__contains=isuse)
    else:
        form = gdzcForm()
        result = gdzcinfoModel.objects.all()

    tableinfo = []
    indx = 0
    for item in result:
        indx += 1
        tmpinfo = [`indx`]
        if len(item.name) > 10:
            tmpinfo.append(item.name[:9] + "...")
        else:
            tmpinfo.append(item.name)
        if len(item.modeltype) > 8:
            tmpinfo.append(item.modeltype[:7] + '...')
        else:
            tmpinfo.append(item.modeltype)
        tmpinfo.append(item.nums)
        tmpinfo.append(item.buydate.isoformat())
        tmpinfo.append(item.adminclass)
        tmpinfo.append(item.adminpp)
        if len(item.demo) > 10:
            tmpinfo.append(item.demo[:2] + "...")
        else:
            tmpinfo.append(item.demo)
        tmpinfo.append(item.isuse)
        tmpinfo.append(item.id)
        tableinfo.append(tmpinfo)

    tablehead = ['序号', '名称', '型　　　　号', '数量', '入 帐 日 期', '归属科室', '责任人', '详细备注', '是否在用', '修改']
    # tableinfo = ['', '', '', '', '', '', '', '', '']
    # tableinfo = [name, phone, personnums, gameclass, startdate, starttime]
    return render_to_response('select.html', {'form':form, "tablehead":tablehead, "tableinfo":tableinfo, 'totalnums':indx})
