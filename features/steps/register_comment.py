from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@given('Exists comment registered by "{username}"')
def step_impl(context, username):
    from authentication.models import User
    user = User.objects.get(username=username)
    from SmartNewsApp.models import Comment
    for row in context.table:
        comment = Comment(user=user)
        for heading in row.headings:
            setattr(comment, heading, row[heading])
        comment.save()

@when(u'I register comment')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('comment_create'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()

@then(u'I\'m viewing the details page for comment by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from SmartNewsApp.models import Comment
    comment = Comment.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(comment)

@then(u'There are {count:n} comments')
def step_impl(context, count):
    from SmartNewsApp.models import Comment
    assert count == Comment.objects.count()

@when('I edit the comment with description "{description}"')
def step_impl(context, description):
    from SmartNewsApp.models import Comment
    comment = Comment.objects.get(description=description)
    context.browser.visit(context.get_url('comment_edit', comment.pk))
    if context.browser.url == context.get_url('comment_edit', comment.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()
