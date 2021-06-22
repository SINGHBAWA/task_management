#  Install system requirements
* `sudo apt-get update && sudo apt-get install python3-pip virtualenv  python3-dev libmysqlclient-dev python3-mysqldb`


##  Mysql Prerequisite
 *   `sudo apt-get update && sudo apt install mysql-server`


###  Mysql Setup

* `sudo chown mysql /var/run/mysqld`
* `sudo mysqld_safe --skip-grant-tables`
* `sudo mysql --user=root mysql`
* `mysql>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';flush privileges;`
* Create database and update credentials `settings.py`
* dump database using  `mysql -u [user] -p testdb<testdb.dmp`


## Virtual environment

* `pip3 install virtualenv`
* `virtualenv -p python3 env`
* `source env/bin/activate`
 

## Django setup

* `git clone -b development <respository-url>`
* `cd task_management`
* `pip3 install -r requirements.txt`


## Add User groups:

Add superuser User
* `python manage.py createsuperuser`

Add Users and assign Groups:
* login to django admin (http://127.0.0.1:8000/admin)
    Add groups:
    ```
        Client
        Manager
        Employee
    ```

    Add Users and assign groups from admin panel.
 