
from django.contrib import admin
from django.urls import path,include
from company_app import urls as company_urls
from employee_app import urls as employee_urls
from assets_app import urls as asset_urls
from asset_tracking_app import urls as asset_log_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(company_urls, namespace='company_app')),
    path('', include(employee_urls, namespace='employee_app')),
    path('', include(asset_urls, namespace='assets_app')),
    path('', include(asset_log_urls, namespace='asset_tracking_app')),
]

