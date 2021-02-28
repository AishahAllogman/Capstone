# Capstone _ Final project in Fsnd

## Intro 

Capstone  is  final project   in Full stack nanodegree from Udacity  
in this project creating moives and managing and assing actors 

 with that roles :

1) Casting Assistan: Can view actors and movies
2) Casting Director: All permissions a Casting Assistant has and,
Add or delete an actor from the database,Modify actors or movies
3) Executive Producer: All permissions a Casting Director has and,Add or delete a movie from the database



## Backend
this application has just backend for now 
### Getting Started
API endpoints can be accessed via (https://git.heroku.com/capstone-aisha.git)

Auth0 information for endpoints that require authentication can be found in **setup.sh**
## Api Tasks

### error Endel 
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
•	400: Bad Request
•	404: Resource Not Found
•	422: Not Processable
    401:  Unauthorized
    500: Internal Server Error

## Endpoint : 
**GET /Movies**
•	General:
	Returns a list of Moive  objects, success value
  requires get:movies permission

•	Sample Request: https://git.heroku.com/capstone-aisha.git/movies 
•   Sample Response
```
{
    "movies": [],
    "success": true
}
```
**GET /Actors** 
•	General:
  Returns a list of Actors   objects, success value
  requires get:actors permission
•	Sample: https://git.heroku.com/capstone-aisha.git/actors 
•   Sample Response
```
{
    "actors": [],
    "success": true
}
```
**Post/Movies**
•	General:
 Creates a new movie using the submitted json parameter ( id, name,relasedate)
  Returns the json object ( id, name,relasedate)
  requires post:movies permission

•	Sample Request: https://git.heroku.com/capstone-aisha.git/moives
     Request Body  
     ```
     {
    "id": 1,
    "title": "miracles from Heaven",
    "release_data":"23April2021 "
     }
     ```
•   Sample Response
 ```
{
    "movie": [
        {
            "id": 1,
            "release_data": "Fri, 23 Apr 2021 00:00:00 GMT",
            "title": "miracles from Heaven"
        }
    ],
    "success": true
}
 ```
**Post/Actors** 
•	General:
 Creates a new Actors using the submitted json parameter ( id, name,age, and gender)
 Returns the json object ( success value,id, name,age, and gender)
  requires post:actors permission
•	Sample: https://git.heroku.com/capstone-aisha.git/actors
    Request Body  
     ```
     {
    "id": 1,
    "name": "Ali",
    "age": 30,
    "gender":"male"
      }
    ```
•   Sample Response
     ```
    "actor": [
        {
            "age": 30,
            "gender": "male",
            "id": 1,
            "name": "Ali"
        }
    ],
    "success": true  
      ```
**Patch/Movies**
•	General:
 Edit  the movie   given  ID if it existsusing the submitted json parameter (  name,relasedate)
  Returns the json object ( id, name,relasedate)
  requires patch:movies permission

•	Sample Request: https://git.heroku.com/capstone-aisha.git/moives/1
     Request Body  
     ``` 
     {
    "title":"Aishamoives",
    "release_data":"3june2009"
    }
     ```

•   Sample Response
```
{
    "movie": [
        {
            "id": 1,
            "release_data": "Wed, 03 Jun 2009 00:00:00 GMT",
            "title": "Aishamoives"
        }
    ],
    "success": true
}
```
**patch/Actors** 
•	General:
 Edit  the actor   given  ID if it existsusing the submitted json parameter (  name,age,gender)
  Returns the json object ( id, name,age,gender)
  requires post:actors permission
•	Sample: https://git.heroku.com/capstone-aisha.git/actors/1
    Request Body  
 ```
{
    "name":"sweet",
    "gender":"f"
}
 ```
  
•   Sample Response
    ```
{
    "actor": [
        {
            "age": 25,
            "gender": "f",
            "id": 2,
            "name": "sweet"
        }
    ],
    "success": true
}
     ```
**Delete /Movies**
•	General:
	Deletes the Movies of the given  ID if it exists. Returns the json object ( id of the deleted movie, success value)
  requires delete:movies permission

•	Sample Request: https://git.heroku.com/capstone-aisha.git/moives/1 
•   Sample Response
   ```
{
    "detele": 3,
    "success": true
}
 ```

**Delete/Actors** 
•	General:
  Deletes the Actor of the given  ID if it exists. Returns the json object ( id of the deleted actors, success value)
  requires delete:actors permission
•	Sample: https://git.heroku.com/capstone-aisha.git/actors/1 
•   Sample Response
 ```
{
    "detele": 2,
    "success": true
}
 ```
## if you want to working with application locally 
 [locall]()
## Testing
To run the tests, run
```
dropdb Capstone
createdb Capstone 
python testapp.py
```

