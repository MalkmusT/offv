# -*- coding: utf-8 -*-


import openfoodfacts



def search ( querry ):
   search_result = openfoodfacts.products.search(query)
   return search_result

