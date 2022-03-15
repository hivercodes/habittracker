import requests
from datetime import datetime

PIXELA_ENDPOINT_USER = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(PIXELA_ENDPOINT_USER, json=params)
#print(response.text)


graph_params = {
    "id": "graph1",
    "name": "Days programmed",
    "unit": "Commits",
    "type": "int",
    "color": "momiji"
}


graph_endpoint = f"{PIXELA_ENDPOINT_USER}/{USERNAME}/graphs"

#create_graph = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(create_graph.text)


post_pixel_endpoint = f"{graph_endpoint}/graph1"


now = datetime.now()

post_params = {
    "date": now.strftime("%Y%m%d"),
    "quantity": "3",
}




#post_pixel = requests.post(url=post_pixel_endpoint, json=post_params, headers=headers)
#print(post_pixel.text)


update_endpoint = f"{post_pixel_endpoint}/{now.strftime('%Y%m%d')}"

update_params = {
    "quantity": "15"
}

update = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(update.text)