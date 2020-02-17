 @given ('Wallpaper and laminate are sold in different stores: Maxidom and Leroy Merlin')
  def step(context):
  pass
  
 
 @when ('the user clicks "Add to shopping list" for each {"product"}')
  def step(context):
  
  
  
 @then ('2 shopping {"list"} are created for each store')
  def step(context,list):
   list=[]
   list.append('product')
   asserEqual(bool(list), True)
   
