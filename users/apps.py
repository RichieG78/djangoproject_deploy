from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = "users"

    def ready(self):                #ADDED
        import users.signals        #HERE: imports signals.py 
 