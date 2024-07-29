# Root Level

The `manage.py` file is a command-line utility in Django projects. It provides various commands to help manage the project, such as running the development server, creating database tables, and running tests. You can execute commands using the following syntax:

```
python manage.py <command>
```

Some commonly used commands include:

- `runserver`: Starts the development server.
- `makemigrations`: Creates new database migration files based on changes in your models.
- `migrate`: Applies pending database migrations.
- `createsuperuser`: Creates a new superuser for the admin interface.
- `test`: Runs the project's test suite.

To see a full list of available commands, you can run `python manage.py help`. Make sure to navigate to the project's root directory before executing any `manage.py` commands.


# Install and configure Tailwind CSS in your Django app

If you want to use Tailwind CSS inside your Django project, there's something called django-tailwind. You can find the documentation on https://pypi.org/project/django-tailwind/

- If you're using uv, it might be difficult for you to actually install tailwind because uv is new framework and lacks support for tailwind. So it's recommended to install tailwind using pip, but how??

- You can run either of the following commands in the terminal to install pip
  ```bash
  python -m pip install --upgrade pip
  ```
  or

  ```bash
  python -m ensurepip --upgrade 
  ```

- The above commands would have installed pip in your system. Now you can run the following commands directly from pip. Remember to not execute the commands using uv pip, instead use pip directly

  ```bash
  pip install django-tailwind
  ```

  ```bash
  pip install 'django-tailwind[reload]'
  ```

- Inside your project folder, open the `settings.py` file and under INSTALLED_APPS, add `"tailwind"`

- Now, you have to initialize the tailwind app using another command. cd to your root folder and execute
  
  ```bash
  python manage.py tailwind init
  ```

- Keep the project name same as `theme` (Recommended)

- Register the generated `theme` app to INSTALLED_APPS in `settings.py`
  ```python
  TAILWIND_APP_NAME = 'theme'
  ```

- The tailwind runs on a different instance of server, so you need to provide the `INTERNAL_IPS`. You can do this by adding the following line to your `settings.py` file
  ```python
  INTERNAL_IPS = ['127.0.0.1'] 
  ```

- Install Tailwind CSS dependencies, by running the following command:
  `python manage.py tailwind install`

- You might get an error this time, saying you don't have `npm` installed on your machine. You can resolve this by adding another line to your `settings.py` file.

  For windows: 
  ```python
  NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
  ```
  For macOS or Linux:
  ```python
  NPM_BIN_PATH = '/usr/local/bin/npm'
  ```

- Try running the command again, and this time your tailwind css will install the dependencies successfully.

- Now, all you need to do is to conifigure auto-reload: django_browser_reload which automatically refreshes the browser when a change is saved

- Again, go to `setting.py` and under INSTALLED_APPS, add 
  ```python
  'django_browser_reload' 
  ```
- Another thing you need to do at this point is to add a middleware under MIDDLEWARE
  ```python
  "django_browser_reload.middleware.BrowserReloadMiddleware"
  ```

- Hey hey hey, this is not it. You need to now go to the `urls.py` file of your project directory and add another path to it. Make sure to add it at the end.
   ```python
   urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
   ]
   ```

- Finally, you should be able to use Tailwind CSS classes in HTML. Open another instance of terminal and start the development server by running the following command:
   ```bash
   python manage.py tailwind start
   ```

### You're good to go!!
- For further details, refer to https://django-tailwind.readthedocs.io/en/latest/installation.html



#
# How to use Tailwind CSS in HTML?
By now, you would have successfully installed and configured Tailwind CSS in your project. All that is left is to use it in HTML files. Let's do it

- Open your layout.html file and on the very top add:
  ```html
  {% load static tailwind_tags %}
  ```

- In the head element, add:
  ```html
  <head>
  {% tailwind_tags %}
  </head>
  ```

### You can now use Tailwind CSS classes in your templates.