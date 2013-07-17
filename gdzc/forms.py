#coding:utf8
from django import forms
from models import gdzcinfoModel
import datetime

class gdzcForm(forms.Form):
    yearslst  = [("", ""),]
    [yearslst.append((`i`,`j`)) for i,j in zip(range(1993,2013), range(1993,2013))]
    yearslst = tuple(yearslst)
    uselst = (("", ""), ("在用","在用"), ("闲置","闲置"), ("报废","报废"))
    dateyear    = forms.ChoiceField(required=False, choices = yearslst, label='年份')
    adminpp     = forms.CharField(required=False, label='责任人', widget= forms.TextInput())
    demo        = forms.CharField(required=False, label='详细备注', widget= forms.Textarea())
    isuse       = forms.ChoiceField(required=False, choices = uselst, label='是否在用')
    adminclass  = forms.ChoiceField(required=False, label='归属科室')

    def __init__(self, *args, **kwargs):
        super(gdzcForm, self).__init__(*args, **kwargs)
        departlst = gdzcinfoModel.objects.values('adminclass')
        tuple_departlst = [("", "")]
        for idepart in departlst:
            tmptuple = (idepart["adminclass"], idepart["adminclass"])
            if tmptuple not in tuple_departlst:
                tuple_departlst.append(tmptuple)
        tuple_departlst = tuple(tuple_departlst)
        self.fields['adminclass'].choices = tuple_departlst

    # class Meta:
    #     model = gdzcinfoModel
    #     fields = ('admin', 'phone', 'personnums',)

    def clean(self):
        return self.cleaned_data
