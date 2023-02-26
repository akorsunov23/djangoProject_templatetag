from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'app_templatetags/index.html'
