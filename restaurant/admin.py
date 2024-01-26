from django.contrib import admin
from .models import Restaurant
from .models import Menu
from .models import MenuItem

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)