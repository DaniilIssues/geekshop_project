import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UserCreate.as_view(), name='user_create'),
    path('users/read/', adminapp.UsersList.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.UserUpdate.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UserDelete.as_view(), name='user_delete'),

    path('categories/create/', adminapp.ProductCategoryCreate.as_view(), name='category_create'),
    path('categories/read/', adminapp.ProductCategoryList.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdate.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(), name='category_delete'),

    path('products/read/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_read'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/update/<int:pk>/', adminapp.ProductUpdate.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDelete.as_view(), name='product_delete'),

    path('visual_site/read/', adminapp.VisualSite.as_view(), name='visual_sites'),
    path('visual_site/create/', adminapp.VisualSiteCreate.as_view(), name='visual_create'),
    path('visual_site/update/<int:pk>', adminapp.VisualSiteUpdate.as_view(), name='visual_update'),
    path('visual_site/delete/<int:pk>', adminapp.VisualSiteDelete.as_view(), name='visual_delete'),
]


