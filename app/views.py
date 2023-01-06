from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import OrderForm
from app.serializers import OrderFormSerializer


def index(request):
    catalogs = OrderForm.objects.all()
    context = {
         'catalogs': catalogs.order_by('user_name'),
    }
    return render(request, 'app/index.html', context=context)


def answer(request, user):
    ans = OrderForm.objects.get(user_name=user)
    return render(request, 'app/answer.html', {'ans': ans})


class OrderFormViewSet(ModelViewSet):
    queryset = OrderForm.objects.all()
    serializer_class = OrderFormSerializer

    def list(self, request, *args, **kwargs):
        user_name = request.GET.get('name')
        if user_name:
            self.queryset = self.queryset.filter(user_name=user_name)

        user_email = request.GET.get('email')
        if user_email:
            self.queryset = self.queryset.filter(user_email=user_email)

        serial = self.get_serializer(self.queryset, many=True)
        return Response(serial.data)
