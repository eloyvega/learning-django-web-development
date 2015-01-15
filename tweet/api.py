from tastypie.resources import ModelResource
from tweet.models import Tweet

from tastypie.authentication import BasicAuthentication

class TweetResource(ModelResource):
    class Meta:
        queryset = Tweet.objects.all()
        resource_name = 'tweet'
        authentication = BasicAuthentication()