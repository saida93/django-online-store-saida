from django.contrib import admin
from django.urls import path
from products.views import products_view, main_view, product_detail_view,categories_view
from django.conf.urls.static import static
from djangoOnlinestoreSaida import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('categories/', categories_view)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
