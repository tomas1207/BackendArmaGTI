from rest_framework import serializers
from . import models as user
class RegisterNewUser(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    
    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = user.NewUser
        fields = ('email','user_name', 'password','steamID','vestName')
        extra_kwargs = {'password':{'write_only':True}}