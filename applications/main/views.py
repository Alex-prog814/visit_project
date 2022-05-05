from rest_framework.views import APIView
from rest_framework.response import Response
from applications.main.models import TradePoint
from applications.main.serializers import TradePointSerializer, VisitSerializer


class TradePointView(APIView):

    def post(self, request):
        trade_points = TradePoint.objects.filter(worker__phone_number=request.POST.get('phone_number'))
        serializer = TradePointSerializer(trade_points, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):

    def post(self, request):
        data = request.POST
        serializer = VisitSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
