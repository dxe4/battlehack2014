from datetime import datetime
import json

from django.shortcuts import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from theapp.models import UserRequest, User, UserResponse
from theapp.payments import TokenPurchase


def make_json_response(data):
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


def get_user(email):
    return User.objects.get_or_create(email=email)[0]


class _CsrfView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(_CsrfView, self).dispatch(*args, **kwargs)


class CreateRequest(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        expires = datetime.fromtimestamp(int(data['expires']))

        user = get_user(data['from_user'])
        user_request = UserRequest(
            lon=data['lon'], lat=data['lat'], message=data['message'],
            expires=expires, user=user)
        user_request.save()

        data = {'status': 'ok', 'id': user_request.id}
        return make_json_response(data)


class CreateResponse(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])

        user_request = UserRequest.objects.get(pk=data['request_id'])
        user_response = UserResponse(
            text=data['text'], user_request=user_request, user=user)
        user_response.save()

        data = {'status': 'ok', 'id': user_response.id}
        return make_json_response(data)


class ListResponses(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])
        user_responses = UserResponse.object.filter(
            user_request__user=user)

        data = [(i.id, i.text) for i in user_responses]
        return make_json_response(data)


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
            user.tokens -= user.response.bounty
            user.save()
            user_response.user.tokens += user.response.bounty
            user_response.user.save()
            user_response.accepted = True

        data = {'status': 'ok'}
        return make_json_response(data)


class FindNearest(_CsrfView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST
        city, lon, lat = data['city'], data['lon'], data['lat']
        result = UserRequest.objects.find_closest(city, lon, lat)

        data = {'status': 'ok', 'result': result}

        return make_json_response(data)


class PurchaseTokens(_CsrfView):
    http_method_names = ['post', 'get']

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = get_user(data['from_user'])
        nonce = data['nonce']
        amount = data['amount']

        if not user:
            return HttpResponse(status=400)
        elif not nonce:
            return TokenPurchase.generate_client_token(user)
        else:
            return TokenPurchase.buy(nonce, user, amount)
