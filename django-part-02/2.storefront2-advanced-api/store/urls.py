from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from pprint import pprint

router = routers.DefaultRouter()

# router = SimpleRouter()
# router = DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
# pprint(router.urls)

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

urlpatterns = router.urls + products_router.urls


# urlpatterns = [
# path('', include(router.urls)),
# path("products/", views.ProductList.as_view()),
# path("products/<int:pk>/", views.ProdcutDetail.as_view()),
# path("collections/", views.CollectionList.as_view()),
# path(
#     "collections/<int:pk>/",
#     views.CollectionDetail.as_view(),
#     name="collection-detail",
# ),
# ]
