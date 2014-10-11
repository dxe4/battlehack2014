import json

from django.shortcuts import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from theapp.models import UserRequest


class CreateRequest(View):
    http_method_names = ['post']

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CreateRequest, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_request = UserRequest(data['lon'], data['lat'], data['message'],
                                   data['expires'], data['from_user'])
        data = {'status': 'ok', 'id': user_request.uid}

        return HttpResponse(
            json.dumps(data),
            content_type="application/json")
