from rest_framework import serializers

class SimpleSerializer(serializers.Serializer):
    name=serializers.CharField()
    description =serializers.CharField()
    phone_number=serializers.IntegerField()
    is_alive=serializers.BooleanField()
    amount=serializers.FloatField()
    extra_name=serializers.CharField()
    created_at =serializers.DateTimeField()
    updated_at =serializers.DateTimeField()
       
        