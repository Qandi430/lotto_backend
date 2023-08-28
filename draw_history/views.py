from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import DrawHistory
from .serializers import DrawHistorySerializer
from .services import getLottoByApi

# Create your views here.
class DrawHistoryViewSet(ModelViewSet):
    queryset = DrawHistory.objects.all()
    serializer_class = DrawHistorySerializer

    @action(detail=False,methods=['POST'])
    def callApi(self,request):
        print('call api')
        getLottoByApi()
        return Response({"status" : 200})
    
    @action(detail=False,methods=['GET'])
    def getLast(self,request):
        print('get last')
        queryset = DrawHistory.objects.last()
        serializer = DrawHistorySerializer(queryset)
        return Response(serializer.data)

    # def list(self,request):
    #     queryset = DrawHistory.objects.all()
    #     print(queryset)
    #     serializer = DrawHistorySerializer(queryset,many = True)
    #     return Response(serializer.data)

    # def create(self,request):
    #     print("draw history create")
    #     pass

    # def retrieve(self,request,draw_no=None):
    #     print("draw history retrieve")
    #     pass

    # def update(self,request):
    #     print("draw history update")
    #     pass

    # def destroy(self,request):
    #     print("draw history destroy")
    #     pass
