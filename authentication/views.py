from authentication.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
 	form_class = UserCreationForm
 	success_url = reverse_lazy('login')
 	template_name = 'sign_up.html'

class LogIn(generic.CreateView):
 	form_class = AuthenticationForm
 	success_url = reverse_lazy('login')
