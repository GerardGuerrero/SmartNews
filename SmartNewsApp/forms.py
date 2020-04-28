from django.forms import ModelForm
from SmartNewsApp.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ()
