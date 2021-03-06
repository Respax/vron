# vron
A little connector between 2 APIs: Viator &amp; RON.

Main features:

- Allows Respax tours to be available for Viator
- Logs every request with error handling (It makes 5 new attempts)
- Sends email notifications when sensitive errors occurs
- Responsive Admin Area with API settings and log of requests received and made


### Technologies and Tools Used

#### Back-End
- Python >= 3.4
- Django >= 1.7
- MySQL >= 5.4

#### Front-End
- HTML
- CSS
- Javascript

#### IDE of preference
- PyCharm
- Sublime

#### Server Side
- Ubuntu 14.0.4
- Vagrant
- Virtual Box
- GIT
- Celery

#### APIs
- [RON Api](http://wiki.respax.com.au/respax/ron_api)
- [Viator API](http://supplierapitestharness.viatorinc.com/documentation.php)


### Installing required software

1. Install Vagrant (Go to: http://www.vagrantup.com/downloads.html)
2. Install Virtual Box (Go to: https://www.virtualbox.org/wiki/Downloads)
3. Install GIT, including command line options. (Go to: http://git-scm.com/downloads)
4. Install Python 3.4 (Go to: https://www.python.org/)


### Cloning the code

1. Clone the GIT Repository using the following command:
    `git clone https://github.com/humbertomn/vron.git ~/vron`

    PS: If you want to install anywhere on your system, change the path: "~/vron"

2. To start up your virtual environment, run the following command:
    ```
    cd ~/vron/infra
    vagrant up
    ```
    Vagrant is configured to use the ports 2222, 8080, 8181 and 4443, so make sure they are free to be used.

3. If you see an error message that starts with 'Failed to mount folders in Linux guest' run the following commands:
    ```
    vagrant ssh
    sudo groupadd vron-dev
    sudo usermod -a -G vron-dev vagrant
    sudo usermod -a -G vron-dev www-data
    exit
    vagrant reload
    ```

4. Run the following command to configure your environment (Make sure you still in the 'infra' folder).
    `python helper.py config site on local with database`

    The helper.py script will install all needed packages on your local enviroment, such as apache, git and also a local mysql database. It will ask to you the root's password for the database (Choose one that is good to you. We will use "88uhGLua19UOSAmav" for examplification).


### Installing the database
1. Connect to the virtual machine via SSH:
    `python helper.py connect local` or `vagrant ssh`

2. Access your mysql and create a database called 'vron'
    `mysql -u root -p`
    When asked for the password, type in: 88uhGLua19UOSAmav

3. Create the database 'vron' and the user 'vron':
    ```
    create database vron;
    create user vron@localhost identified by '99pUq3PAwFjnBsdZe3';
    grant all on vron.* to vron@localhost;
    exit;
    ```

4. Activate your python virtualenv and run a 'migrate' inside your django application:
    ```
    source /vronvenv/bin/activate
    python /vron/django/manage.py migrate
    ```

5. Create a superuser to be able to access the admin area
    ```
    source /vronvenv/bin/activate
    python /vron/django/manage.py createsuperuser
    ```


### Testing
To make sure it works open up [http://localhost:8080/]
