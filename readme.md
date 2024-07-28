# Learning Django

## Installation
Installation of django is quite simple, you have two options to install it, the first one is the traditional approach using the existing 
``` pip install Django ``` command. The other one is:

- If this is the very first time you are working with Django on this machine, you need to install uv which is a virtual environment that makes your production faster and easier

- To install uv:
    
  If you are on windows, run the following command:
  
  ```powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  ```

  else if you are on macOs or Linux, use:

  ``` curl -LsSf https://astral.sh/uv/install.sh | sh ```

  You can find the uv documentation on https://pypi.org/project/uv/

- After installing uv, restart your terminal or better would be to restart your PC and type ``` uv venv ``` to create the virtual environment. Again it's not mandatory to do it this way, you can run ``` py -m venv .venv ``` too.

- By now, the last command would have added a .venv folder to your project directory. Now, you can activate the environment by running ``` .venv\Scripts\activate ``` on windows or ``` source .venv/bin/activate ``` on macOs or Linux.

- Once, you have activated your environment, you need install django to your virtual environment, and you can do this by ``` uv pip install Django ``` . Make sure the D of Django is capital and the command starts with uv.

- Now, all you need is to start a project, and you can do this using ``` django-admin startproject project_name ``` Replace project_name with the name of your project

- If you followed these steps precisely, you should now be able to see a folder into your root directory with the same name as your project

- All you need to do now is to start your development server by running ``` py manage.py runserver ``` command on the terminal.

- Your project should now be running on localhost:8000

- It's possible that your port 8000 might already being used by some other application. In this case, you can run the  ``` py manage.py runserver port_number ``` Boom! that's it. You just need to add a port number to the previous command and you're ready to go.

#
# Levels in Django

## Project Level

The project level in Django refers to the top-level directory that contains your entire Django project. It typically has the same name as your project and serves as the main entry point for your application.

At the project level, you will find important files such as `settings.py`, which contains the configuration settings for your project, and `urls.py`, which defines the URL patterns for your project.

## Root Level

The root level in Django refers to the directory that contains your entire Django project, including any additional files or directories that are not part of the Django framework itself. This can include files such as READMEs, requirements.txt, or any other project-specific files.

The root level is often the parent directory of the project level directory. It provides a convenient place to store project-related files that are not directly related to the Django framework.

## App Level

The app level in Django refers to individual applications within your Django project. Each app represents a specific functionality or feature of your project. For example, you might have separate apps for user authentication, blog posts, or product listings.

At the app level, you will typically find files such as `models.py`, which defines the database models for the app, `views.py`, which contains the logic for handling HTTP requests, and `templates/`, which stores the HTML templates for rendering the app's views.

By organizing your project into separate apps, you can achieve modularity and reusability, making it easier to maintain and extend your Django project.
