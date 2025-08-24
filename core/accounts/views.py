from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

class CustomRegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    redirect_authentication_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super(CustomRegisterView, self).get(*args, **kwargs)
    