#pip install git+https://github.com/behave/behave

from behave import *

@given('I am finding a tile with "{price}" less than 1000 rub/m2, the "{strengh}" is higher then 6, the "{usage}" is higher then 6')
   def step_impl(context):
   assert context.table is not None

@when('When I launch a search for all stores')
def step_impl(context,name,price,strengh,usage):
for price<1000 and strengh>6 and c>6:
   assert_that(context.name, equal_to(product))
   assert_that(context.number1, equal_to(price))
   assert_that(context.number2, equal_to(strengh))
   assert_that(context.number3, equal_to(usage))
 

@then('Then there are 2 variants of the tile that meet the requirements with the articles 1001 and 1002')
def step_impl(context,name, number1, number2, number3)
    print("Product:%s, Price: %s, Streght: %s, Usage: %s" % (name, number1,number2, number3))
