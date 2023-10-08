# PricingModuleV2

# 1. clone the project from repository
# 2. create a virtual env in your system using command python3 -m venv venvname
# 3. activate the venv
# 4. install all the packages from file requirements.txt using pip install -r requirements.txt
# 5. run the below commands
  # 1. python manage.py makemigrations
  # 2. python manage.py migrate
  # 3. python manage.py createsuperuser
  # 4. pyton manage.py runserver

# 6. go to the any browser and hit localhost:8000 or 127.0.0.1:8000
# 7. login for the admin UI -> hit localhost:8000/admin/ or 127.0.0.1:8000/admin/
# 8. login with the credentials which you created user as a superuser
# 9. import the excel files which is attached to this repository to save your time instead of adding record from admin panel UI

# 10. Here is the cURL snippet for API

  curl --location --request POST 'localhost:8000/api/get-price/' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "time_taken": "3 hour",
      "day": "Monday",
      "distance_traveled_in_km": 5,
      "waiting_time": "0 min"
  }'
# 11. import this is postman for testing
