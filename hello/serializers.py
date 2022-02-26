from rest_framework import serializers
from hello.models import Talents

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Talents
        fields=('TalentId','TalentName')