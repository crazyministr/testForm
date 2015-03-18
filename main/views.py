# coding=utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View, FormView, TemplateView
from django.shortcuts import render_to_response
from main.models import User


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['users'] = [{'name': u.name,
                             'salary': u.salary} for u in User.objects.all()]
        return context

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name,
                                  self.get_context_data(),
                                  context_instance=RequestContext(request))

main = MainPageView.as_view()
