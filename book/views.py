from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PaymeWebhookView(APIView):
    """Payme billing tizimi uchun webhook"""
    def post(self, request, *args, **kwargs):
        # Payme'dan kelgan JSON RPC so'rov
        data = request.data
        method = data.get('method')
        
        # TODO: method turi (CheckPerformTransaction, CreateTransaction va h.k) ni tekshirish
        # va Subscription holatini (is_active=True) yangilash.
        
        return Response({"result": {"message": "Success"}}, status=status.HTTP_200_OK)

class ClickWebhookView(APIView):
    """Click billing tizimi uchun webhook"""
    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        
        # TODO: action turi (0 - Prepare, 1 - Complete) ni tekshirish 
        
        return Response({"error": 0, "error_note": "Success"}, status=status.HTTP_200_OK)