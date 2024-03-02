from rest_framework import serializers
from mainSite.models import Trening, TYPE_CHOICES


class TreningSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dOt = serializers.DateField()
    hOt = serializers.TimeField()
    tD = serializers.IntegerField()
    tOw = serializers.ChoiceField(choices=TYPE_CHOICES, default='no-gi')
    hMf = serializers.IntegerField()
    fD = serializers.IntegerField()
    bD = serializers.IntegerField()
    tA = serializers.IntegerField()
    iA = serializers.CharField(required=True)

    def create(self, validated_data):
        return Trening.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.dOt = validated_data.get('dOt', instance.dOt)
        instance.hOt = validated_data.get('hOt', instance.hOt)
        instance.tD = validated_data.get('tD', instance.tD)
        instance.tOw = validated_data.get('tOw', instance.tOw)
        instance.hMf = validated_data.get('hMf', instance.hMf)
        instance.fD = validated_data.get('fD', instance.fD)
        instance.bD = validated_data.get('bD', instance.bD)
        instance.tA = validated_data.get('tA', instance.tA)
        instance.iA = validated_data.get('iA', instance.iA)
        instance.save()
        return instance
    
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trening
        fields = ['owner','dateOfTraining', 'hourOfTraining', 'trainingDuration', 'typeOfWorkout', 'howManyFights', 'fightDuration', 'breakDuration', 'tiredAfter', 'injuriesAfter']