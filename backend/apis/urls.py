from django.urls import path, include
from apis import views

urlpatterns=[
    path('',views.api_home)
    # path('product/',include(product.urls))
]