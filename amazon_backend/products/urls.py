from django.urls import path, include
from .views import ProductList, CategoryViewSet, SellerViewSet, ProductListAPIView
from rest_framework.routers import DefaultRouter



category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'delete': 'destroy',
})

router = DefaultRouter(trailing_slash=False)
router.register('sellers', SellerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductList.as_view()),
    path('products-filter/', ProductListAPIView.as_view()),
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
]