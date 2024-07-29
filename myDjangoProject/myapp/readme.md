# My app

A project can have multiple apps running in it. You can create a new app by simply running the command in root directory terminal ```py manage.py startapp app_name```. Replace app_name with the name of your app.

## Things to do after creating the app

- Although it completely optional to have a separate templates folder inside your app, it is good to have one just for separation of concerns and modularity. Create a templates folder inside your app, and inside the templates folder, create another folder that has the same name as your app.

- You can add your templates files inside it which are basically your HTML files and nothing else. 

- You would notice you will not be getting any emmet suggestions at this point. Simply click ctrl + comma on your keyboard and search emmet

- scroll down to include languages and add django-html and html in the corresponding input boxes. That's it, you will be getting the suggestions now.

- Now, all you need to do is to go to your project folder, and open settings.py file. Go to the key that says Applications and at last, add your app


## How to connect your app to the main project

Connecting your app to the project is definitely not going to be a nightmare for you if you follow the steps given below carefully

- All you need to get started with is a urls.py file at your app level. This urls file will have all your routes. For the start, you can copy the contents from urls.py file in project folder.

- Now, go ahead and remove all the unnecessary paths from the file and just keep the root path that is path("", views.myapp, name="whatever")

- This is the time to connect your app urls to the project.

- In the ```urls.py``` file of the project, import include from django.urls

- Add another path that says ```path('chai\', include('your_app.urls'))``` Now you might be thinking how does the project knows about your app

- This is where settings.py comes into play, open ```settings.py``` file and scroll down to ```INSTALLED_APPS``` and add the name of your project at the very end.

### urls.py file at project level

```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('chai/', include('myapp.urls')),
]
```

### urls.py file at app level
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allChai, name="all-chai"),

]
```

## Template engine in Django
If you are coming from javascript, you might have worked with react where you can have a layout and all your children components are rendered within it. You can do the same in Django as well. 

- Go to the templates folder at the root level and add layout.html file there.

- Add the boilerplate code using ! and on the very top add ``` {% load static %} ```

- Link your CSS using traditional link tag

   ```html
    <link rel='stylesheet' href="{% static 'style.css'%}">
    ```
- You might want each page to have its own title, so what you can do is, add a unnamed block inside your title tag. This block behaves like a placeholder

   ```html
    <title>
        {% block title %}
        Here you can give a default value if you want
        {% endblock %}
    </title>
    ```
- Similarly, you can add a block to the body as well under your navbar
  ```html
  <body>
    <nav>This is your Navbar</nav>
    {% block content %}{% endblock %}
  </body>
  ```

## How to render elements within this layout?

To render your elements within this layout, you just have to create your template (HTML file)

- Go to your app level templates --> your_app_name --> Create a file here

- Inside that file, on the very top, you need to inherit from the layout (basically extend your layout file)

- add this line: ```{% extends 'layout.html' %}```. Now how does my project knows where is this layout file?? The answer is django will check each and every templates folder and find layout.html and once it finds it, it will extend it in the template file

- Now, if you remember, we had two unnamed blocks in our layout file, one was title and other was content. What you need to do is, go ahead and add those two unnamed blocks here as well

```html
{% extends 'layout.html' %}

{% block title %}
My app title
{% endblock %}

{% block content %}
<h1>Welcome to my app</h1>
{% endblock %}
```

- You are good to go.
