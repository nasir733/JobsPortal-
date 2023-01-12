from django.http import HttpResponse
from users.models import UserDeviceInfo
import ua_parser.user_agent_parser as user_agent_parser

class IpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        user_ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        parsed_user_agent = user_agent_parser.Parse(user_agent)
        # print(parsed_user_agent['os']['family'])
        device_type='mobile'
        if (parsed_user_agent['os']['family'] == "Mac OS X" or parsed_user_agent['os']['family'] == "Windows"):
            device_type='desktop'
        
        UserDeviceInfo.objects.create(user_ip=user_ip, device_type=device_type)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
