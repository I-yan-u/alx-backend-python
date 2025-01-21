from datetime import datetime
import logging

from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(filename='../request.log', level=logging.INFO,
                            format='%(message)s')

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path} - Method: {request.method}"
        
        logging.info(log_message)

        response = self.get_response(request)
        return response
    
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time().strftime("%H")
        if current_time != datetime.strptime("21", "%H").time() or current_time != datetime.strptime("06", "%H").time():
            return HttpResponseForbidden("Access not allowed at this time")
        response = self.get_response(request)
        return response