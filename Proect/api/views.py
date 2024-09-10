import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions, viewsets, generics
from api.models import CustomUser, Role, StripeCustomer, MonthlyOutput
from api.serializers import UserCreateSerializer, UserSerializer, UserDataSerializer, UserUpdateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.utils.dateparse import parse_date
from django_filters import rest_framework as filters
from django.utils import timezone
import json

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Utility functions for output management
def check_user_output(user):
    today = timezone.now().date()
    output_record, created = MonthlyOutput.objects.get_or_create(user=user, date=today)
    return output_record.output_count < 100  # Example limit

def increment_user_output(user):
    today = timezone.now().date()
    output_record, created = MonthlyOutput.objects.get_or_create(user=user, date=today)
    output_record.output_count += 1
    output_record.save()

# User registration
@api_view(['POST'])
def register_view(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Get the first role with name 'User'
            role, created = Role.objects.get_or_create(name='User')
            if role is None:
                return Response({"error": "Role 'User' not found"}, status=status.HTTP_404_NOT_FOUND)

            user.role = role
            user.save()

            # Create Stripe customer
            stripe_customer = stripe.Customer.create(
                email=user.email,
                name=f"{user.first_name} {user.last_name}",
            )
            StripeCustomer.objects.create(
                user=user,
                stripeCustomerId=stripe_customer.id,
            )

            user_data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'role': user.role.name if user.role else None
            }

            return Response({
                'message': 'User registered successfully',
                'data': user_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# User login
@api_view(['POST'])
def login_view(request):
    """
    Authenticate and login the user.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        token_data = {
            'token': token.key,
            'role': user.role.name if user.role else None
        }

        return Response({
            'message': 'Login successful',
            'data': token_data,
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# User logout
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Logout successful"})

# Create Stripe checkout session
@csrf_exempt
@api_view(['POST'])
def create_checkout_session(request):
    """
    Create a Stripe checkout session.
    """
    YOUR_DOMAIN = "http://localhost:8002"
    try:
        data = json.loads(request.body)
        amount = data.get('amount')  # Сумма должна быть получена от клиента

        if not amount:
            return JsonResponse({'error': 'Amount is required'}, status=400)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Subscription',
                        },
                        'unit_amount': amount,  # Сумма в центах
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{YOUR_DOMAIN}/success/',
            cancel_url=f'{YOUR_DOMAIN}/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)

# User filters for filtering users by date joined
class UserFilter(filters.FilterSet):
    date_joined_after = filters.DateFilter(field_name='date_joined', lookup_expr='gte')
    date_joined_before = filters.DateFilter(field_name='date_joined', lookup_expr='lte')

    class Meta:
        model = CustomUser
        fields = ['date_joined_after', 'date_joined_before']

# ViewSet for users
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

# Create user view
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

# Current user view
class CurrentUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserDataSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin CRUD operations for users
@csrf_exempt
@api_view(['GET'])
def user_list(request):
    """
    List users with pagination and optional date filters.
    """
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))
    date_joined_after = request.GET.get('date_joined_after')
    date_joined_before = request.GET.get('date_joined_before')

    users_query = CustomUser.objects.all()

    if date_joined_after:
        users_query = users_query.filter(date_joined__gte=parse_date(date_joined_after))
    if date_joined_before:
        users_query = users_query.filter(date_joined__lte=parse_date(date_joined_before))

    total_users = users_query.count()
    users = users_query[(page - 1) * page_size: page * page_size]

    data = {
        "results": list(
            users.values('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', role_name='role')),
        "count": total_users
    }

    return JsonResponse(data)

@csrf_exempt
@api_view(['POST'])
def user_create(request):
    """
    Create a new user.
    """
    data = request.data

    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if password != confirm_password:
        return JsonResponse({"error": "Passwords do not match"}, status=400)  # Bad Request

    role, created = Role.objects.get_or_create(name='User')  # Default role

    user = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email, role=role)
    user.set_password(password)
    user.save()

    return JsonResponse({"id": user.id}, status=201)

@csrf_exempt
@api_view(['PUT'])
def user_update(request, user_id):
    """
    Update an existing user.
    """
    data = request.data

    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)  # Not Found

    user.username = data.get('username', user.username)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)

    # Note: Password is not updated for security reasons
    user.save()

    return JsonResponse({"id": user.id})

@csrf_exempt
@api_view(['DELETE'])
def user_delete(request, user_id):
    """
    Delete a user.
    """
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return JsonResponse({"message": "User deleted"}, status=204)  # No Content
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)  # Not Found
