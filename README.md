# WHT.Agency

## Installation
1. Clone this repository:

    ```
    git clone https://github.com/Kasatello/wht.agency.git
    ```
 2. Create .env file and define environmental variables following .env.sample:
    ```
    DJANGO_SECRET_KEY=Create yours at https://djecrety.ir/
    DEBUG=1 for Debug view
    POSTGRES_HOST=your db host
    POSTGRES_DB=name of your db
    POSTGRES_USER=username of your db user
    POSTGRES_PASSWORD=your db password
    ```
    
### To run it from docker
1. Run command:
      ```
      docker-compose up --build
      ```

## Used technologies
    - Django Rest Framework
    - PostgreSQL
    - Docker

## Endpoints
    "teams": "http://0.0.0.0:8080/api/teams/teams/",
    "user register": "http://0.0.0.0:8080/api/user/register/",

