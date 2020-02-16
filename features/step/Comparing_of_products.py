#pip install git+https://github.com/behave/behave

from behave import *

@given('I am finding a tile with "{number1}" less than 1000 rub/m2, the "{number2}" is higher then 6, the "{number3}" is higher then 6')
   def step_impl(context):
   pass

@when('When I launch a search for all stores')
def step_impl(context):
    context.browser.get('??')
    form = get_element(context.browser, tag='form')
    get_element(form, name="msisdn").send_keys('??')
    form.submit()

@then('Then there are 2 variants of the tile that meet the requirements with the articles 1001 and 1002')
def step_impl(context, number1, number2, number3):
    if number1 < "1000" and number2 > "6" and number3 > "6":
    assert_that (
