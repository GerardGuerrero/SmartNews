from behave import *
import operator
from functools import reduce
from django.db.models import Q

@when(u'I delete the comment with description "{description}"')
def step_impl(context, description):
    from SmartNewsApp.models import Comment
    comment = Comment.objects.get(description=description)
    comment.delete()
