import requests
import json

url = "http://127.0.0.1:8000/PizzaApi/"

url_for_fetching = "http://127.0.0.1:8000/PizzaApi/getPizza/"


def create_pizza_entry(type, size, toppings):
    data = {
        "Type": type,
        "size": size,
        "Toppings": toppings
    }

    h = {
        'Content-Type': 'application/json'
    }

    d = json.dumps(data)

    r = requests.post(url, data=d, headers=h)

    response = r.json()
    print(response)


def delete_pizza_entry(id):
    data = {
        "id": id,
    }

    h = {
        'Content-Type': 'application/json'
    }

    d = json.dumps(data)

    r = requests.delete(url, data=d, headers=h)

    response = r.json()
    print(response)


def update_pizza_entry(data):
    h = {
        'Content-Type': 'application/json'
    }

    d = json.dumps(data)

    r = requests.put(url, data=d, headers=h)

    response = r.json()
    print(response)


def fetch_piza_entries(pageno, size=None, type=None):
    params = {
        "size":size,
        "type":type,
        "page":pageno
    }

    h = {
        'Content-Type': 'application/json'
    }

    r = requests.get(url_for_fetching,params=params,headers=h)
    response = r.json()
    print(response)



#fetch_piza_entries(1,type="regular",size="small")

#create_pizza_entry("Regular","small",["corn","cheese","done"])
# delete_pizza_entry(1)

'''
update_pizza_entry({
    'id':5,
    'Type':'square',
    'Toppings':{
        'add_Topping':True,
        'data':['fuck',"cheese"]
    }
})
'''


