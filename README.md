# 2019 coop uk trip timeline app

A simple django app made to demonstrate building apis with django-rest-framework

## Running

### With docker

1. Install docker and docker compose (follow the instructions for your platform https://docs.docker.com/compose/install/)

1. Start the server and dependencies

        docker-compose up

1. Run database migrations (docker-compose must be running, so use a separate terminal)

        docker-compose exec web python manage.py migrate 
        
1. Collect static files and build frontend code

        docker-compose exec web python manage.py collectstatic
        docker-compose exec -w /code/frontend web yarn build frontend 
        
1. Create a superuser (this user will have access to the admin interface)

        docker-compose exec web python manage.py createsuperuser

    follow the instructions to create the user
    
1. The app should be now accessible in http://localhost:8000

    you can access the admin to create new timeline entries in http://localhost:8000/admin and logging in with the superuser you created in step 4 
    
