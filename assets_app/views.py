from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import Asset
from .forms import AssetForm
from django.urls import reverse_lazy

class AssetCreateView(CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'assets_app/add.html'
    success_url = reverse_lazy('assets_app:asset_list') 


class AssetListView(ListView):
    model = Asset
    template_name = 'assets_app/all.html'
    context_object_name = 'assets'

class AssetUpdateView(UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'assets_app/add.html'
    success_url = reverse_lazy('assets_app:asset_list') 
    
class AssetDetailView(DetailView):
    model = Asset
    template_name = 'assets_app/view.html'
    context_object_name = 'asset'

class AssetDeleteView(DeleteView):
    model = Asset
    template_name = 'assets_app/assets_app_confirm_delete.html'
    success_url = reverse_lazy('assets_app:asset_list')
