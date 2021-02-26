# PizzaAssignment


## Api endpoints 

* ### For fetching ("http://127.0.0.1:8000/PizzaApi/getPizza/") 

Users can fetch filtered list of pizza  based on size or type of pizza from this endpoint
input format for sending request to backend is given below
```
 data = {              
   "size":size,         
   "type":type,
   "page":pageno
 }  
```
 add data as query params in get request  , here **size** and **type** are optional fields for filtering  but **page** is mandatory and it  represents the page number for paginating large amount of pizza's

 response from server is as follows 
 ```
 response = {              
   'count': 1, 
   'next': 'http://127.0.0.1:8000/PizzaApi/getPizza/?page=2&size=small&type=square',
   'previous': None,
   'results': [    {'Type': 'square',
                     'size': 'small',
                     'Toppings': [{'name': 'cheese'}, {'name': 'tomato'}]}
                 , {'Type': 'square',
                     'size': 'small',
                     'Toppings': [{'name': 'onion'}, {'name': 'corn'}]}
              ]
 }  
```
here 
1. count represents the total number of pizza's present in database according to the  size and type which user has requested 
2. next represnts  the url for fetching next set of results 
3. previous represents  the url for fetching  previous page 
4. results  is having the real data which  contain list of pizza 
5. inside each pizza its type ,size and list of toppings are given

**Note** size of pagination is  set to 2 for testinf purpose you can chanhge its value in  [settings.py](https://github.com/ajitsinghrathore/PizzaAssignment/pizza_project/settings.py)file



 
 
       
       
