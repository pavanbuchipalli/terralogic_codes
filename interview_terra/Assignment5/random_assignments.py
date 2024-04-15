import random

details ={}
locations =["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]
employess =int(input("Select how many No Of employess Requried :---"))
def get_details():
    for i in range(1,employess+1):
        id = random.randrange(1,9999)
        location = random.choice(locations)
        salary = random.randint(20000,150000)
        details[i]={"employee_id" :id,
                    "locations":location,
                    "salaryes" :salary}
        yield details[i]

obj=get_details()
print(obj.__next__())
for i in obj:
    print(i)



