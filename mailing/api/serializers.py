from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from mailing.settings import LEN_CODE, MAX_HOUR_UTC, MIN_HOUR_UTC, LEN_PHONE
from notification.models import CodeMobileOperator, Client, Message, Mailing


class CodeMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeMobileOperator
        field = '__all__'

    def validate_code(self, code):
        if len(code) != LEN_CODE:
            raise serializers.ValidationError(
                'Размер телефонного кода должен быть равен 3.'
            )
        return code


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        field = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    code_mobile_operator = CodeMobileSerializer()

    class Meta:
        model = Client
        field = '__all__'

    def validata_phone(self, phone):
        if len(phone) != LEN_PHONE:
            raise serializers.ValidationError(
                'Длина номера телефона должна содержать 10 символов.'
            )
        return phone

    def validate_utc(self, utc):
        if utc > MAX_HOUR_UTC or utc < MIN_HOUR_UTC:
            raise serializers.ValidationError(
                'Значение часового пояса должно быть в интервале'
                ' от -12 до +14.'
            )
        return utc


class MessageSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer(read_only=True, )
    client = ClientSerializer(read_only=True, )

    class Meta:
        model = Message
        field = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    total_number_of_mailings = SerializerMethodField()
    total_send_msg = SerializerMethodField()

    def get_total_number_of_mailings(self):
        pass

    def get_total_send_msg(self):
        pass


class DetailStatisticSerializer(serializers.ModelSerializer):
    pass
