

from django.contrib import admin
from django.urls import path
from posts.views import main, now_date, goodbye

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('goodbye/', goodbye),
    path('now_date/', now_date)
]
