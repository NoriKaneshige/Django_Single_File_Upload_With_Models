from django.urls import reverse_lazy
from django.views import generic
from .forms import SingleUploadModelForm
from .models import UploadFile


class SingleUploadWithModelView(generic.CreateView):
    """ view to upload file model """
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')

class FileListView(generic.ListView):
    """ view for page listing all uploaded files """
    model = UploadFile