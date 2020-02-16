Feature: Comparing of products
   I want to compare features and prices of different products in different stores.

  Scenario: product display with minimal price among stores
    Given I am findind a tile with price <1000 rub/m2, the strength is higher then 6, the usage is higher then 6.
     When I launch a search for all stores
     Then there are 2 variants of the tile that meet the requirements with the articles 1001 and 1002
     And the tiles with article 1001 is specified a shop "Petrovich" with the price - 239 rub/m2
     And the tile with article 1002 is specified a shop "Leroy Merlin" with the price 518 rub/m2

  Scenario: Selection of shops 
     Given tile with article 1001 is on an opened page. 
     When a user clicks the button "view in other stores" 
     Then a page is opened with a list of stores, where the tile is in the presence,and prices for article 1001
     And there is in the store "Petrovich" with price 239 rub/m2, stock availability is 10 m2.
     And there is in the store "Maxidom" with price 400 rub/m2, stock availability is 300 m2.
