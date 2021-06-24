from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .services.permissions import AdminAccess


class UserRedirectView(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return reverse_lazy('user:index_admin')

class IndexAdminView(AdminAccess, generic.TemplateView):
    template_name = 'admin/index.html'


class MenuView(AdminAccess, generic.TemplateView):
    pass
