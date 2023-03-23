from rest_framework import serializers

from notification.models import CodeMobileOperator, Client, Message, Mailing


class CodeMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeMobileOperator
        field = '__all__'

    def validate_code(self, value):
        pass


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        field = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    code_mobile_operator = CodeMobileSerializer()

    class Meta:
        model = Client
        field = '__all__'

    def validate_utc(self, value):
        pass


class MessageSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer(read_only=True, )
    client = ClientSerializer(read_only=True, )

    class Meta:
        model = Message
        field = '__all__'
