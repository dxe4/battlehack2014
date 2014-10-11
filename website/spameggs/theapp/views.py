from datetime.datetime import fromtimestamp
import json

from django.shortcuts import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from theapp.models import UserRequest, User, UserResponse


class _CsrfView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CreateRequest, self).dispatch(*args, **kwargs)


class CreateRequest(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        expires = fromtimestamp(int(data['expires']))

        user = User.objects.get_or_create(email=data['from_user'])
        user_request = UserRequest(
            lon=data['lon'], lat=data['lat'], message=data['message'],
            expires=expires, user=user)
        data = {'status': 'ok', 'id': user_request.id}

        return HttpResponse(
            json.dumps(data),
            content_type="application/json")


class CreateResponse(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = User.objects.get_or_create(email=data['from_user'])

        user_request = UserRequest.objects.get(pk=data['request_id'])
        user_response = UserResponse(
            text=data['text'], user_request=user_request, user=user)

        data = {'status': 'ok', 'id': user_response.id}
        return HttpResponse(
            json.dumps(data),
            content_type="application/json")
