from rest_framework import routers

from posts.views import PostViewSet

app_name = "posts"

router = routers.DefaultRouter()
router.register("", PostViewSet)

urlpatterns = router.urls
