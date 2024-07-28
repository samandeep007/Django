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

### Enjoy!!!