**School Management System**
This is a Django+Bootsrap project
<br>
<br>

**Getting Started**
<br>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
<br>

**Prerequisites**
<br>
Python 3
PostgreSQL

<br>

**Installing**
<br>
Create a postgresql database schooldb, and a user with superuser privileges to own the database, by default the credentials can be the same as the username and password in env.sh.template: 
<br>
*export DATABASE_URL = postgres://schooluser:<password>@localhost:5432/schooldb*

sudo -u postgres createuser schooldbuser --superuser
*$ sudo -u postgres psql*

*postgres=# ALTER USER schooldbuser WITH PASSWORD 'Utu@123';*

*postgres=# \q*

Create the database

*sudo -u postgres createdb schooldb -O schooldbuser*
Migrate the database

*python manage.py migrate*
