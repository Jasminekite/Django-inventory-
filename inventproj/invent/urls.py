# invent/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # Category Management
    path('add-category/', views.add_category, name='add_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('update-category/<int:id>/', views.update_category, name='update_category'),

    # Item Management
    path('add-item/', views.add_item, name='add_item'),
    path('delete-item/<int:id>/', views.delete_item, name='delete_item'),
    path('update-item/<int:id>/', views.update_item, name='update_item'),

    # Transaction Management
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('delete-transaction/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('update-transaction/<int:id>/', views.update_transaction, name='update_transaction'),

    # Supplier Management
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('delete-supplier/<int:id>/', views.delete_supplier, name='delete_supplier'),
    path('update-supplier/<int:id>/', views.update_supplier, name='update_supplier'),
]
