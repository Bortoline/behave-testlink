# Created by jframos at 1/7/16


from behave import step


@step(u'the number "{num:d}"')
def given_number(context, num):
    context.num1 = num


@step(u'I add the given number number to "{num:d}"')
def add_number(context, num):
    context.result = context.num1 + num


@step(u'the result is "{num:d}"')
def check_result(context, num):
    assert context.result == num, "ERROR: The result is not the expected one"

