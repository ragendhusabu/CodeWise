from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb
from Repository.serializers import QuestionSerialoizer

# Create your views here.



class QuestionsDbCreateView(APIView):
    def get(self,request):
        qs = QuestionsDb.objects.all()
        serializer_instance =QuestionSerialoizer(qs,many = True)
        
        return Response(data = serializer_instance.data)



    def post(self,request):
        form_data = request.data
        serializer_instance = QuestionSerialoizer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionsDb.objects.create(**actual_data)
            return Response(data ={ "Message" : "Question Added Succesfully"})
        else:
            return Response(data ={"errors" : serializer_instance.errors})

class QuestionsRetrieveUpdateDelete(APIView):

    def get(self,request,pk):

        qs = QuestionsDb.objects.get(id=pk)
        serializer_instance = QuestionSerialoizer(qs)

        return Response (data =serializer_instance.data)

    def put(self,request,pk):

        form_data = request.data

        serializer_instance = QuestionSerialoizer(data = form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.filter(id=pk).update(**actual_data)
            return Response(data = serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors())

    def delete(self,request,pk):

        QuestionsDb.objects.filter(id=pk).delete()

        return Response({"Message" : "Deleted. Successfully"})