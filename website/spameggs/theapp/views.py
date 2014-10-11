from datetime.datetime import fromtimestamp
import json

from django.shortcuts import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from theapp.models import UserRequest, User, UserResponse


def make_json_request(data):
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


def get_user(email):
    return User.objects.get_or_create(email=email)


class _CsrfView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CreateRequest, self).dispatch(*args, **kwargs)


class CreateRequest(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        expires = fromtimestamp(int(data['expires']))

        user = get_user(data['from_user'])
        user_request = UserRequest(
            lon=data['lon'], lat=data['lat'], message=data['message'],
            expires=expires, user=user)

        data = {'status': 'ok', 'id': user_request.id}
        return make_json_request(data)


class CreateResponse(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])

        user_request = UserRequest.objects.get(pk=data['request_id'])
        user_response = UserResponse(
            text=data['text'], user_request=user_request, user=user)

        data = {'status': 'ok', 'id': user_response.id}
        return make_json_request(data)


class ListResponses(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])
        user_responses = UserResponse.object.filter(
            user_request__user=user)

        data = [(i.id, i.text) for i in user_responses]
        return make_json_request(data)


class AcceptAnswer(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])
        response_id = data['response_id']

        user_response = UserResponse.object.get(pk=response_id)
        if not user_response.request.user.id == user.id:
            return HttpResponse(status=403)
        else:
            user_response.accepted = True

        data = {'status': 'ok'}
        return make_json_request(data)


class FindNearest(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        city, lon, lat = data['city'], data['lon'], data['lat']
        result = UserRequest.objects.find_closest(city, lon, lat)

        data = {'status': 'ok', 'result': result}
        return make_json_request(data)
