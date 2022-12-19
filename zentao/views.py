from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View, TemplateView


class BugView_0(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello, getn')

class BugView(TemplateView):
    # 模板文件名
    template_name = 'BugView.html'

    # 获取模板中数据
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['name'] = 'BugView'
        kwargs['title'] = "BugView"
        return kwargs
