import requests
from datetime import datetime

profile_page = "https://pixe.la/@boma"  # the account has already been created
USERNAME = "boma"
TOKEN = "yy44466tdggjfff7"
GRAPH_ID = "graph1"

date = datetime(year=2024, month=1, day=20)
formatted_date = date.strftime("%Y%m%d")

user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
delete_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
user_parameters = {
    "token": "yy44466tdggjfff7",
    "username": "boma",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# post request to create user ie post new user details to external service
# response = requests.post(url=user_endpoint, json=user_parameters)
# print(response.text)

graph_parameters = {
    "id": "graph1",
    "name": "Python Self Study",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}
http_headers = {
    "X-USER-TOKEN": TOKEN
}
# Post request to create a new graph and provide authentication
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=http_headers)
# print(response.text) # to print the result to know if successful or not

# Now goto https://pixe.la/v1/users/boma/graphs/graph1.html to view the new graph
# from step 3, in the url https://pixe.la/v1/users/a-know/graphs/test-graph, replace a-know
# with the username, test-graph with the graph ID then add .html


post_pixel_parameters = {
    "date": formatted_date,
    "quantity": "17.3"
}

# Post request to make an entry into the graph. NB entry is a pixel
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=http_headers)
# print(response.text)

# Put request to update an already existing pixel or create a new one if it does not exist
pixel_update_parameter = {
    "quantity": "7.8"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameter, headers=http_headers)
# print(response.text)

# Delete pixel
response = requests.delete(delete_endpoint, headers=http_headers)
print(response.text)