from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from onlinerating.api_views import QuestionnaireViewSet, EmployeeFeedbackViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("questionnaire", QuestionnaireViewSet)
router.register("employee-feedback", EmployeeFeedbackViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("onlinerating/", include("onlinerating.urls")),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include("rest_framework.urls"))
]
