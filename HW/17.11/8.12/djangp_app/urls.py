from django.urls import path
from djangp_app.views import export_to_excel

urlpatterns = [
    path('export-to-excel/', export_to_excel, name='export_to_excel'),
]
