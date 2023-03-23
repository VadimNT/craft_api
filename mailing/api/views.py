from rest_framework.viewsets import ModelViewSet

from api.serializers import (ClientSerializer, MailingSerializer,
                             MessageSerializer, )
from notification.models import Client, Mailing, Message


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingViewSet(ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    def statistics(self, request):
        pass

    def detail_statistics(self, request, pk):
        pass


class MessageViewSet(MailingViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
