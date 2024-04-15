import requests
import json
end_points = 'http://localhost:3000/employess'

class Api:
    def Get_request(self):

        get_method= requests.get(end_points)
        print("Status code of the url  :- ",get_method.status_code)
        fetch_data = get_method.json()
        print(fetch_data)
        print("length of data  :- ",len(fetch_data))
        print("url of the file  :- ",get_method.url)
        print("---------------------------------------------------------------------------------------------------------------")

    def Post_request(self):
        data2 = {
            "Name": "zamanoj333",
            "Department": "Development1",
            "Salary": 29000,
            "project": "LPUh"
        }

        Post_method= requests.post(end_points, data=data2)
        print("Hello this the output of post_request")
        print(Post_method.json())
        self.Get_request()

    def Put_request(self):
        data3 ={"id": 7,"Name": "harish","Department": "Testing","Salary": 230000,"project": "LPU"}
        Put_method = requests.put(end_points+"/7",data=data3)
        print("Hello this the output of put_request")
        # print(Put_method.status_code)
        self.Get_request()

    def Delete_request(self):
        data_id = int(input("please provide id number to delete  the data :- "))
        delete_method = requests.delete(end_points+"/{}".format(data_id))
        print("Hello this the output of delete_request")
        self.Get_request()


ss= Api()
ss.Get_request()
ss.Post_request()
ss.Put_request()
ss.Delete_request()

# ss.Get_request()

