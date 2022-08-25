from rest_framework import serializers


class BaseMailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=64)
    subject = serializers.CharField(max_length=256)
    message = serializers.CharField(max_length=2048)
    from_email = serializers.EmailField(max_length=64)


class MailSerializer(BaseMailSerializer):
    pass


class MassMailSerializer(BaseMailSerializer):
    email = serializers.ListField(max_length=10000)
