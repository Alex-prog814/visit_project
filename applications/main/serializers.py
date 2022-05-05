from rest_framework import serializers

from applications.main.models import TradePoint, Worker, Visit


class TradePointSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradePoint
        fields = ('worker', 'title')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['worker'] = instance.worker.name
        return rep


class VisitSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=100, required=True)
    trade_point = serializers.CharField(max_length=100, required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)

    class Meta:
        model = Visit
        fields = ('phone_number', 'trade_point', 'latitude', 'longitude')

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        trade_point = TradePoint.objects.get(title=attrs.get('trade_point'))
        if Worker.objects.filter(phone_number=phone_number).exists():
            if trade_point.worker.phone_number != phone_number:
                raise serializers.ValidationError('The employee is not affiliated with the trade point!')
        else:
            raise serializers.ValidationError('No employee found with this phone number!')
        return attrs

    def create(self, validated_data):
        validated_data['trade_point'] = TradePoint.objects.get(title=validated_data.get('trade_point'))
        visit = Visit.objects.create(**validated_data)
        return visit

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('phone_number')
        rep['worker'] = f'{instance.trade_point.worker}'
        rep['date'] = instance.date
        return rep
