import requests

BASE = "http://127.0.0.1:5000/"
# data = [{"views":100000,"name":"Joe","likes":78},
#         {"views":80000,"name":"How to make REST API","likes":10000},
#         {"views":2000,"name":"Zack","likes":10}]
# for i in range(len(data)):
#     response = requests.put(BASE + "video/"+str(i),data[i])
#     print(response.json())
#
#
# input()
# response = requests.get(BASE + "video/2")
# print(response.json())

response = requests.patch(BASE+"video/2", {'views':99,'likes':101})
print(response.json())