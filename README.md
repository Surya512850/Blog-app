# Blog-app
This is a Blog application which is developed using Django, a python framework. This application enables users to create, read, update and delete blog posts with authentication. Furthermore, the previous versions of each blog post are available. These versions are stored each time the user saves the post. All the updates of that will be reflected in the database.

## Requirements ##

- [x] Python 3
- [x] Django version 4.1.3

## Usage ##

If you want to see the project in action, create a python virtual environment in your projects directory through the command line.
Make sure you have Python installed on your device.

```shell
py -m venv [Your virtual env name]
```

Activate your virtual environment 

```shell
[virtual env]/Scripts/activate
```

Install django using pip command. 

```shell
pip install django 
```

In this repository, the main code is in the blog_app folder. For safety purposes, the SECRET_KEY in settings.py file is removed. 
So, start your own project by 

```shell
django-admin startproject YourProjectName
```
The rest of the code is same. As you create a new project, a new db.sqlite file is created. To use this file for the code in this repository,
the changes to the models must be reflected in the database.

```shell
py manage.py makemigrations
py manage.py migrate
```

For the text editor feature in the body of the blog post, ckeditor is used. Install it by

```shell
pip install django-ckeditor
```

Make sure all the apps (blog, users, ckeditor) are in the INSTALLED_APPS in settings.py file. 
Refer to the settings.py file for changes regarding templates and redirect urls. 
To run the project on your machine, type

```shell
py manage.py runserver [port no Optional]
```

All the above commands are for windows. 

