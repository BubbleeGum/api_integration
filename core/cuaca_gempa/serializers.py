from rest_framework import serializers

class CuacaGempaParamsTimes(serializers.Serializer):
    type = serializers.CharField()
    # h = serializers.CharField()
    datetime = serializers.CharField()
    # value = serializers.CharField()

class CuacaGempaSerializer(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField()
    times = CuacaGempaParamsTimes(many=True)

    

