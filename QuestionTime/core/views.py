from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class IndexTemplateview(LoginRequiredMixin, TemplateView):
    """Index Template View for authenticated users"""
    login_url = '/account/login/'

    def get_template_names(self):
        template_name = "index.html"
        return template_name
