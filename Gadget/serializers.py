from rest_framework import serializers
from .models import Gadget

class GadgetSerializer(serializers.ModelSerializer):
    class Meta:             
        model = Gadget
        fields = '__all__'
        
    def validate_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError('title length more than 50')
        return value
    
    def validate(self, attrs):
        # self.validate_title(attrs['title'])
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)