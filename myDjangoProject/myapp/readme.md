# My app

A project can have multiple apps running in it. You can create a new app by simply running the command in root directory terminal ```py manage.py startapp app_name```. Replace app_name with the name of your app.

## Things to do after creating the app

- Although it completely optional to have a separate templates folder inside your app, it is good to have one just for separation of concerns and modularity. Create a templates folder inside your app, and inside the templates folder, create another folder that has the same name as your app.

- You can add your templates files inside it which are basically your HTML files and nothing else. 

- You would notice you will not be getting any emmet suggestions at this point. Simply click ctrl + comma on your keyboard and search emmet

- scroll down to include languages and add django-html and html in the corresponding input boxes. That's it, you will be getting the suggestions now.

- Now, all you need to do is to go to your project folder, and open settings.py file. Go to the key that says Applications and at last, add your app