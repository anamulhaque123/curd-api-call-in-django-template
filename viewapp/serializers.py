from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def Validate(self, attr):
       data = super().Validate( attr)
       token =self.
        # Add custom claims
       token['name'] = user.name
        # ...

        return token