# Roomies API 
This repository contains the code which provides the API endpoints necessary to allow the Roomies application to retrieve and store its data. 

# Planning & Design 

## Database Design 
![Roomies DB Diagram](readme_images/db-diagram.png)

## API Goals 
* Allow users to register/login to the Roomies app 
* Allow users to create `Household`'s, which is the primary model that connects all the functionality of the app. 
* Allow users to add/remove other users to their `Household`
* Allow users to create `Grocery Lists` for their `Household`
* Allow users to add `Grocery Items` to their `Grocery Lists`
* Allow users to add `Comments` to their `Grocery Lists`
* Provide CRUD functionality for the database models created 


# Technologies Used 
* Django 
* Python 
* ElephantSQL 
* Django Rest Framework
* Django Rest Auth 
* Django Filters 

# Features 

## Households 
I have created API's to allow users to interact with `Household` related functionality. Below is a list of the endpoints that the React application can access: 

| Endpoint        | HTTP Methods     | Description  |
| --------------- | ---------------- | ------------ |
| `/households`   | `GET`, `POST`    | Allow users to list households and create new households |
| `/households/:id` | `GET`, `DELETE`, `PUT` | Allow users to retrieve, delete, or update a single household | 
| `/households/:id/members` | `GET`, `POST` | Allow users to list or add members to their household | 
| `/households/:id/members/:memberId` | `GET`, `PUT`, `DELETE` | Allow users to retrieve, update, or delete a member of a household |
| `/households/:id/availableusers` | `GET` | Allow users to retrieve a list of the possible members that can be added to a household |
| `/households/:id/markrentdue` | `POST` | Allow household creators to mark the rent of their household as due. |

### Example
Below is a screenshot from the API showing an example of one of the above API's 
![Household API Example](readme_images/household-example.png)

## Grocery Lists
I have also created API's to allow users to manage `Grocery Lists` for their household. Below is a list of endpoints that the React application can access:

| Endpoint        | HTTP Methods     | Description  |
| --------------- | ---------------- | ------------ |
| `/grocerylists`   | `GET`, `POST`    | Allow users to list grocery lists and create new grocery lists |
| `/grocerylists/:id`   | `GET`, `DELETE`, `PUT`    | Allow users to retrieve, update, or delete a single grocery list |
| `/groceryitems`   | `GET`, `POST`    | Allow users to list grocery items for a particular list, as well as create new ones. |
| `/groceryitems/:id`   | `GET`, `PUT`, `DELETE`    | Allow users to retrieve, update, or delete a particular grocery list item |
| `/grocerylistcomments`   | `GET`, `POST`    | Allow users to list the comments for a particular grocery list as well as create new ones. |
| `/grocerylistcomments/:id`   | `GET`, `PUT`, `DELETE`    | Allow users to retrieve, update, or delete a particular grocery list comment |

### Example
Below is a screenshot from the API showing an example of one of the above API's 
![Grocery List API Example](readme_images/grocery-example.png)

## Authentication and Permissions 

### Authentication 
The use of the API is restricted to authenticated users only. Users who have not logged in will receive a `HTTP 403` if they try and access the API without logging in. 

### Permissions 
I have created several custom permissions which allows me to further restrict access to the data, beyond just ensuring that the user has logged in. They have been detailed below. 

| Name            | Description  |
| --------------- |------------ |
| `IsCreatorOrReadOnly`   | Allows write access to a model if the current user is the `creator`, otherwise read-only access.    |
| `CanManageHousehold`   | Allows read/write access to a `Household` model if the user is either the `creator` or exists in the `members` relation list    |
| `CanManageGroceryList`   | Allows read/write access to a `GroceryList` model if the user is either the `creator` or exists in the `members` relation list of the `Household` associated with the list.   |
| `CanManageGroceryItem`   | Allows read/write access to a `GroceryListItem` model if the user is either the `creator` or exists in the `members` relation list of the `Household` associated with the list that the item belongs to.   |

# Agile Development 
I have created a Github project to track the user stories for the entire application (API and UI) and that can be viewed [here](https://github.com/users/ilaria-barletta/projects/3/views/1)

# Deployment, Forking and Cloning 

## Deployment
The project has been deployed using Heroku. Here are the step to follow for the deployement:

1. Access your Heroku account and click on "create a new app", name the app and select the region before hitting the create app button.   
2. Navigate to the settings tab and create config vars for cloudinary, the database, and the secret key
3. Navigate to the deploy section and select Github as deployment method. After confirming that we want to connect to Github we can then search for the Github repository name. Once we find it we can click on connect. 
5. Scroll down and select enable automatic deploys

The live link to my project is here: https://roomiesapi-637170cefd22.herokuapp.com/



## Forking & Cloning
To fork this repository click on the "Fork" button in the top right of the repository in Github. 

To clone this repository:
1. Click the "Code" button in the repository. 
2. Copy the clone link.
3. Use git to clone the copied link: `git clone LINK`. 

___
# References & Credits
* TBD