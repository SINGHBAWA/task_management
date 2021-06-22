from tasks.views import TaskCreateListUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TaskCreateListUpdateView, basename='task')
urlpatterns = router.urls