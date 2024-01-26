from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

        import stripe
        stripe.api_key = "Ohjelmoijat_ovat_viisaita"
        
        charge = stripe.PaymentIntent.create(
            amount=int(serializer.validated_data['amount'] * 100),
            currency="usd",
            payment_method=serializer.validated_data['payment_method'],
            confirm=True,
        )

        # Update the payment status based on the Stripe response
        if charge['status'] == 'succeeded':
            serializer.instance.payment_status = 'completed'
        else:
            serializer.instance.payment_status = 'failed'

        serializer.instance.save()
