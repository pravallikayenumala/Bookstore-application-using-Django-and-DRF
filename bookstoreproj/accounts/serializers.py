from rest_framework import serializers 
from .models import CustomUser
from rest_framework_simplejwt import serializers as jwt_serializer


class customeruserserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','phone_number','location']


class Verifyserializer(serializers.Serializer):
    phone_number=serializers.CharField()
    otp=serializers.CharField()

    def validate(self, data):
        phone_number = data.get('phone_number')
        otp = data.get('otp')

        try:

         User=User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("error")
        if not User.check_otp(otp):
            raise serializers.ValidationError("error")
        
        return data

class CustomTokenSerializer(jwt_serializer.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

         

        











