PreRequisites
1. python vesion 3.6 or hugher installed in the system
2. mongo db is up and running in system
3. Django==3.0.5 installed 

steps to setup repo
1. pip install -r requirement.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py loaddata fixtures/product.json
5. python manage.py loaddata fixtures/productdetails.json
6. python manage.py runserver