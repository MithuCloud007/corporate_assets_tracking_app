from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import AssetLog
from .forms import AssetLogForm
from django.urls import reverse_lazy

class AssetLogCreateView(CreateView):
    model = AssetLog
    form_class = AssetLogForm
    template_name = 'asset_tracking_app/add.html'
    success_url = reverse_lazy('asset_tracking_app:asset_log_list') 


class AssetLogListView(ListView):
    model = AssetLog
    template_name = 'asset_tracking_app/all.html'
    context_object_name = 'asset_logs'

class AssetLogUpdateView(UpdateView):
    model = AssetLog
    form_class = AssetLogForm
    template_name = 'asset_tracking_app/add.html'
    success_url = reverse_lazy('asset_tracking_app:asset_log_list') 
    
class AssetLogDetailView(DetailView):
    model = AssetLog
    template_name = 'asset_tracking_app/view.html'
    context_object_name = 'asset_log'

class AssetLogDeleteView(DeleteView):
    model = AssetLog
    template_name = 'asset_tracking_app/asset_tracking_app_confirm_delete.html'
    success_url = reverse_lazy('asset_tracking_app:asset_log_list')
