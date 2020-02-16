Feature: List of products
         I get some list with products for every stores.
         
Scenario: Creating the list
     Given Wallpaper and laminate are sold in different stores: Maxidom and Leroy Merlin
     When the user clicks "Add to shopping list" for each stuff
     Then 2 shopping list are created for each store.
     
Scenario: Update the list 
     Given user has a shopping list for Maxidom
     And a lamp is sold in Maksidom and Leroy
    And the lamp is cheaper in Leroy
     When the user adds a lamp to the list for the Maxidom

Then there is a hint that this lamp is cheaper in Leroy
And it is suggested to add the lamp to the new list for Leroy
