from rest_framework import serializers
from users.models import ExtendedUser
class RegisterNewUser(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('email','user_name','password','vestName','steamID')
        extra_kwargs = {'password':{'write_only':True}}
    def create(self,data):
        password = data.pop('password',None)
        instance = self.Meta.model(**data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
