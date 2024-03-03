from rest_framework import serializers
from mainSite.models import Trening, Zawody, CompFight

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trening
        fields = ['owner','dateOfTraining', 'hourOfTraining', 'trainingDuration', 'typeOfWorkout', 'howManyFights', 'fightDuration', 'breakDuration', 'tiredAfter', 'injuriesAfter']

class ZawodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Zawody
        fields = ['owner','nameOfComp','dateOfComp','place']

class CompFightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompFight
        fields = ['compFight_id','owner','whichComp','resultOfFight','endOfFight']