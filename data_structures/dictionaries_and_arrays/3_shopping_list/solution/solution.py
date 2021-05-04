
from operator import itemgetter
def cheapest_store(grocery_store, shopping_list):
    total_price = 0
    store_dict = {}
    for store in grocery_dict:
        for groccery in shopping_list: 
            if groccery in list(grocery_store[store].keys()):
                total_price += grocery_dict[store][groccery]
            else: 
                total_price +=5
        store_dict[store] = total_price
        total_price = 0    
    
    # sorted_dict = sorted(store_dict.items(), key=lambda x: (-x[1], x[0]))
    # sorted_dict = sorted(store_dict,key=lambda x: x[1])
    # return sorted_dict[0]
    
    min_total = float('inf')
    min_total_store = " "
    for key, val in store_dict.items():
        if min_total > val:
            min_total = val
            min_total_store = key
        elif min_total == val:
            min_total_store = min(min_total_store,key)
    print(store_dict)
    return  min_total_store


            

# grocery_dict = {"Walmart": {"pasta": 2.0,
#                             "bread": 1.5,
#                             "cheese": 6.0,
#                             "ketchup": 3.0,
#                             "salami": 9.0,
#                             "onions": 1.0},
#                 "Thriftys": {"bread": 4.0,
#                              "ham": 6.0,
#                              "salami": 12.0,
#                              "pasta": 1.75,
#                              "mayo": 4.0,
#                              "onions": 2.0,
#                              "ketchup": 3.5}
#                 }
# shopping_list = ["ham", "salami", "ketchup", "mayo", "pasta", "cheese", "tuna"]
# grocery_dict = {"Whole Foods": {"fish": 5.0,
#                                      "meat": 6.0,
#                                      "waffles": 3.0},
#                      "Walmart": {"fish": 5.0,
#                                  "bread": 2.0}
#                     }
# shopping_list = ["pasta", "cheese"]


grocery_dict = {"Whole Foods": {"fish": 5.0,
                                     "meat": 6.0,
                                     "waffles": 3.0}
                    }
shopping_list = ["fish", "bread"]
print(cheapest_store(grocery_dict, shopping_list)) #== "Walmart"