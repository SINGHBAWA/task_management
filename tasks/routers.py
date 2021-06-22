from .views import TaskCreateListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TaskCreateListView, basename='task')
urlpatterns = router.urls