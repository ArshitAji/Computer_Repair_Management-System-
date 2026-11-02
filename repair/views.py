from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from repair.models import CustomerDb, RepairDb
from repair.serializers import CustomerSerializer, RepairSerializer
# Create your views here.
class CustomerView(APIView):
    def get(self,request):
        qs=CustomerDb.objects.all()
        serializer_instance=CustomerSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=CustomerSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class CustomerRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(CustomerDb, id=pk)
        serializer_instance = CustomerSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        customer_object = get_object_or_404(CustomerDb, id=pk)

        serializer_instance = CustomerSerializer(
            instance=customer_object,
            data=form_data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        customer_obj = get_object_or_404(CustomerDb, id=pk)
        customer_obj.delete()

        return Response(data={
            "Message": "Customer Deleted Successfully!.."
        })


class RepairView(APIView):

    def get(self, request):
        qs = RepairDb.objects.all()
        serializer_instance = RepairSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = RepairSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)



class RepairRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(RepairDb, id=pk)
        serializer_instance = RepairSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        repair_object = get_object_or_404(RepairDb, id=pk)

        serializer_instance = RepairSerializer(
            data=form_data,
            instance=repair_object
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        repair_obj = get_object_or_404(RepairDb, id=pk)
        repair_obj.delete()

        return Response(data={
            "Message": "Repair Deleted Successfully!.."
        })
