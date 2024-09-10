from rest_framework import serializers
from api.models import Teacher, Student, StripeCustomer
from api.models import CustomUser, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """
        Check that the passwords match.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Passwords must match."})
        return data

    def create(self, validated_data):
        """
        Create and return a new `CustomUser` instance, given the validated data.
        """
        # Remove the confirm_password field as it's not needed in the user creation
        validated_data.pop('confirm_password', None)
        
        # Handle the role field, if provided, otherwise set default role
        role = validated_data.pop('role', None)
        if role is None:
            # Default to a 'User' role if no role is provided
            role = Role.objects.get(name='User') if Role.objects.filter(name='User').exists() else None

        # Create the user
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            role=role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
     
class StripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripeCustomer
        fields = ['user', 'stripeCustomerId', 'stripeSubscriptionId']
