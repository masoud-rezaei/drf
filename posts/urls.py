from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import HomePageView  ,UserViewSet,PostViewSet

router=SimpleRouter()
router.register('users',UserViewSet,basename="users")
router.register('',PostViewSet,basename="posts")
#router.register('',HomePageView.as_view(),basename="home")

urlpatterns=router.urls
