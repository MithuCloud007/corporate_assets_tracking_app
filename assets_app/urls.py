from django.urls import path
from .views import AssetCreateView,AssetListView,AssetUpdateView,AssetDetailView,AssetDeleteView
app_name='assets_app'

urlpatterns = [
    path('asset-add', AssetCreateView.as_view(), name="asset_add"),
    path('asset-list', AssetListView.as_view(), name="asset_list"),
    path('asset-list-update/<int:pk>', AssetUpdateView.as_view(), name="asset_list_update"),
    path('asset-list-view/<int:pk>', AssetDetailView.as_view(), name="asset_list_view"),
    path('asset-list-delete/<int:pk>', AssetDeleteView.as_view(), name="asset_list_delete"),
]