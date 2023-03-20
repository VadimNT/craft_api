from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from craft_api.mailing.mailing.settings import (MAX_LEN_MSG, LEN_PHONE,
                                                MIN_HOUR_UTC, MAX_HOUR_UTC,
                                                LEN_TAG_NAME_MOBILE_OPERATOR,
                                                LEN_CODE, )


class CodeMobileOperator(models.Model):
    tag = models.CharField(
        verbose_name='Тэг оператора',
        max_length=LEN_TAG_NAME_MOBILE_OPERATOR,
    )
    code = models.SmallIntegerField(
        verbose_name='Код оператора',
        validators=(
            MinValueValidator(
                LEN_CODE,
                'Размер кода оператора должен быть 3 символа.'
            ),
            MaxValueValidator(
                LEN_CODE,
                'Размер кода оператора должен быть 3 символа.'
            )
        )
    )


class Mailing(models.Model):
    datetime_start_mailing = models.DateTimeField(
        verbose_name='Дата и время начала отправки рассылки'
    )
    text = models.CharField(
        verbose_name='Сообщение',
        max_length=MAX_LEN_MSG,
    )
    filter_property_mailing = models.ForeignKey(
        CodeMobileOperator,
        verbose_name='Фильтр операторов',
        related_name='codes',
        on_delete=models.CASCADE,
    )
    datetime_stop_mailing = models.DateTimeField(
        verbose_name='Дата и время окончания отправки рассылки'
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('datetime_start_mailing',)

    def __str__(self):
        return self.text


class Client(models.Model):
    phone = models.SmallIntegerField(
        verbose_name='Телефон клиента',
        validators=(
            MinValueValidator(
                LEN_PHONE,
                'Номер телефона должно содержать 10 символов.'
            )
        )
    )
    tag = models.CharField(
        verbose_name='Тэг оператора',
        max_length=LEN_TAG_NAME_MOBILE_OPERATOR,
    )
    code = models.SmallIntegerField(
        verbose_name='Код оператора',
        validators=(
            MinValueValidator(
                LEN_CODE,
                'Размер кода оператора должен быть 3 символа.'
            ),
            MaxValueValidator(
                LEN_CODE,
                'Размер кода оператора должен быть 3 символа.'
            )
        )
    )
    utc = models.CharField(
        validators=(
            MinValueValidator(
                MIN_HOUR_UTC,
                'Минимальный часовой пояс -12.'
            ),
            MaxValueValidator(
                MAX_HOUR_UTC,
                'Максимальный часовой пояс +14.'
            ),
        )
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('phone',)

    def __str__(self):
        return self.phone


class Message(models.Model):
    datetime_create = models.DateTimeField(
        verbose_name='Время отправки сообщения.',
        auto_now=True,
    )
    status_send = models.BooleanField(
        verbose_name='Статус отправки сообщения',
        default=False,
    )
    mailing = models.ForeignKey(
        Mailing,
        related_name='mailing',
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        related_name='clients',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('datetime_create',)

    def __str__(self):
        return self.mailing.mailing.text
