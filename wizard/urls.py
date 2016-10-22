from django.conf.urls import url, include
from api.tastypieResources import QuestionResource, ChoiceResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(ChoiceResource())


urlpatterns = [
    url(r'^api/', include(v1_api.urls))
]