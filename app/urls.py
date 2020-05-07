from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # file listing page
    path('', views.FileListView.as_view(), name='file_list'),
    # using models
    path('single/upload/model/', views.SingleUploadWithModelView.as_view(), name='single_upload_with_model'),
]
