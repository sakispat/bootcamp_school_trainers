# Assignment 2

The python django project trainer.
The home page a table all trainers where next to each  
name there are two buttons for edit and delete. On deletion it will display the  
message on success in home page.

The create trainer in navbar new trainer, in form trainer, if you press button  
send and do not put any information in the form it will display messages below  
input, if you enter them correctly you will input message successfully.

The edit button will in edit page for upadate trainer.

The search you can put the surname of the trainer for search, if there is  
the instructor will display the trainer it and will display the message for  
successfully if not there will display a message error, and in the search it  
displays the table with the trainers we are looking for where we can use the  
two buttons edit, delete. 

**None**: Update project and add packages python-dotenv, mysqlclient and update trainer views, templates file.

```bash
    # install virtual
    python -m venv venv

    # copy .env
    cp .env.example .env

    # your secret key
    python -c "import secrets;print(secrets.token_urlsafe('your_number_secret_key'))"   # your secret key and cp in .env file

    # install packages
    pip install -r requirements.txt

    # migration
    python manage.py migrate

    # run server
    python manage.py runserver
```
