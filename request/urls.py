from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('api/create/', views.CreateRequest.as_view(), name="request-create"),
	path('api/accept/<int:pk>/', views.AcceptRequest.as_view(), name="request-accept"),
	path('api/cancel/<int:pk>/', views.CancelRequest.as_view(), name="request-cancel"),
	path('api/finish/<int:pk>/', views.FinishRequest.as_view(), name="request-finish"),
	path('api/decline/<int:pk>/', views.DeclineRequest.as_view(), name="request-decline"),
	path('api/specialneeds/last/', views.SpecialNeedsGetLastRequest.as_view(), name="sn-get-last-request"),
	path('api/volunteer/last/', views.VolunteerGetLastRequest.as_view(), name="vn-get-last-request"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
