#install virtual environament
virtualenv -p python3 bakery_env

#activate virtual environment as bakery_env
source book_env/bin/activate

#install required packages

pip install django==1.11.6
pip install djangorestframework





###Implemeted the login page and dashboard page 

http://127.0.0.1:8000/

####   login with below creadential then only you can able to perform CRUD operation on hierarchical

username: shaker
password: admin123

#### logout from the application and redirected to login page

http://127.0.0.1:8000/logout
##############  Note: if you logout from the application you can able to access the data


# below API service for accessing the data and implemented the Basicauthentication
# first login throgh the browser then you can access the below API Services

http://127.0.0.1:8000/api/v1/book/
http://127.0.0.1:8000/api/v1/book/?book_id=64


