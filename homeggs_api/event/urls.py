from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .views import (
#     CompanyList, CompanyDetail, 
#     SalaryList, SalaryDetail
# )

app_name = 'event'

event_urlpatterns = [
    
]

event_urlpatterns = format_suffix_patterns(event_urlpatterns)