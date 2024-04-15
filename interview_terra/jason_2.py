# design your own sample JSON file that represents product information for a product sale website. The JSON file should include details
# such as product name, price, and the number of items . Additionally, you are required to calculate the total amount for all products and
# also provide individual product amounts. and store the details and amount to csv file
import pandas as pd
import json
import csv
A_Dict= """{
        "products":
        [{"name":"laptop",
          "price":10000,
          "Total_quantity":10}, 
         {"name":"Mouse",
         "price":100,
         "Total_quantity":15},
         {"name":"keyboard",
         "price":1000,
         "Total_quantity":20},
         {"name":"Memory_card",
          "price":2000,
          "Total_quantity":25},
         {"name":"charger",
          "price":3000,
          "Total_quantity":22}
         ]}"""


_list = json.loads(A_Dict)
bb= _list["products"]
data_test ={
    'name':[],
    'price':[],
    'Total quantity' : [],
    "Total_amount": []

}

total = 0
for i in range(len(bb)):
    name = bb[i].get("name")
    data_test['name'].append(name)
    price =bb[i].get("price")
    data_test['price'].append(price)
    quantity=  bb[i].get("Total_quantity")
    data_test['Total quantity'].append(quantity)
    total_amount=bb[i].get("price")*bb[i].get("Total_quantity")
    data_test["Total_amount"].append(total_amount)
    # print(total_amount)
    total +=total_amount

print(data_test)

df_test = pd.DataFrame(data_test)
print(df_test)

print("Total amount of all the products is",total)

df_test.to_csv("CSV.data")
