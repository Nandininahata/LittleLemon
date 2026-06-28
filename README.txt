Little Lemon Capstone Project

Run the project:

python manage.py runserver

Authentication

POST
http://127.0.0.1:8000/api-token-auth/

or

POST
http://127.0.0.1:8000/auth/token/login/

API Endpoints

GET
http://127.0.0.1:8000/restaurant/menu/

POST
http://127.0.0.1:8000/restaurant/menu/

GET
http://127.0.0.1:8000/restaurant/menu/1/

PUT
http://127.0.0.1:8000/restaurant/menu/1/

DELETE
http://127.0.0.1:8000/restaurant/menu/1/

GET
http://127.0.0.1:8000/restaurant/bookings/

POST
http://127.0.0.1:8000/restaurant/bookings/

GET
http://127.0.0.1:8000/restaurant/bookings/1/

PUT
http://127.0.0.1:8000/restaurant/bookings/1/

DELETE
http://127.0.0.1:8000/restaurant/bookings/1/

Protected Endpoint

GET
http://127.0.0.1:8000/restaurant/message/