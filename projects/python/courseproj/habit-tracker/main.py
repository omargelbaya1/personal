import requests
from datetime import datetime

parameters_user={
    "token":"snoandoiansoidnason",
    "username":"omargel",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

pixela_endpoint= "https://pixe.la/v1/users/omargel/graphs/habit-graph-1"


headers={
"X-USER-TOKEN":"snoandoiansoidnason"
}

parameters_graph={
    "id":"habit-graph-1",
    "name":"habit_graph_weight",
    "unit":"kilogram",
    "type":"float",
    "color":"kuro",
    "timezone":"GMT",
    "startOnMonday":True
}
#It is a post request, so call it once, you can't create the same user multiple times!, thanks!
# response=requests.post(url="https://pixe.la/v1/users", json=parameters_user)
# print(response.text)

#creating a graph
# response=requests.post(url=pixela_endpoint,json=parameters_graph,headers=headers)
# print(response.text)

#checking graph has been created
# response=requests.get(url=pixela_endpoint,headers=headers)
# print(response.text)

today= datetime.now()
x=today.strftime('%Y%m%d')


parameters_pixel={
    "date":x,
    "quantity":"140.12",
}

# resource=requests.post(url=pixela_endpoint,headers=headers,json=parameters_pixel)
# print(resource.text)

# def test(x:int, y:int)->bool:
#     if x == y:
#         return True
#     else:
#         return x
#
# print(test(2,3))
