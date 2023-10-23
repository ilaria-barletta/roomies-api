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