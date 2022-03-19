from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import User


class UserModelSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
