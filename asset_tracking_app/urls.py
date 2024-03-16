from django.urls import path
from .views import AssetLogCreateView,AssetLogListView,AssetLogUpdateView,AssetLogDetailView,AssetLogDeleteView
app_name='asset_tracking_app'

urlpatterns = [
    path('asset-log/add', AssetLogCreateView.as_view(), name="asset_log_add"),
    path('asset-log/list', AssetLogListView.as_view(), name="asset_log_list"),
    path('asset-log/update/<int:pk>', AssetLogUpdateView.as_view(), name="asset_log_list_update"),
    path('asset-log/view/<int:pk>', AssetLogDetailView.as_view(), name="asset_log_list_view"),
    path('asset-log/delete/<int:pk>', AssetLogDeleteView.as_view(), name="asset_log_list_delete"),
]