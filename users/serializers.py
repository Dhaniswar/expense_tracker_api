from rest_framework import serializers
from authentication.models import User
from django.core.exceptions import ValidationError as DjangoValidationError
import logging
from django.core.validators import validate_email

# from .choices import GENDER_CHOICES
from rest_framework_simplejwt.backends import TokenBackend



logger = logging.getLogger(__name__)





class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    user_name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True,
        required=True,
        style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True,
        required=True,
        style={'input_type': 'password'})
    # gender = serializers.ChoiceField(choices=GENDER_CHOICES)
 

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_name','email', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {
            "password": {"write_only": True},  
        }
        
        
    def validate(self, data):
        try:
            email = data['email']
            phone = data['phone_number']
            
            validate_email(email)
            
            # Check if user exists
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': 'User with this email already exists'}
                )
            
            if User.objects.filter(phone_number=phone).exists():
                raise serializers.ValidationError(
                    {'phone_number': "Phone number already registered"}
                )
                
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    {'password': "Passwords don't match"}
                )
                
            return data
            
        except DjangoValidationError as e:
            raise serializers.ValidationError({'email': str(e)})
        except Exception as e:
            if isinstance(e, serializers.ValidationError):
                raise 
        raise serializers.ValidationError({'non_field_errors': str(e)})


    def create(self, validated_data):
        # Remove confirm_password as we don't need it anymore
        validated_data.pop('confirm_password', None)
        
        # Create new user using your UserManager
        user = User.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_name=validated_data.get('user_name'),
            password=validated_data['password']
        )
        
        return user

        
    def create(self, validated_data):
        email = validated_data.pop('email')
        phone = validated_data.pop('phone_number')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password')
        username = validated_data.pop('user_name')
        
        confirm_password = validated_data.pop('confirm_password')

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'phone_number': phone,
                'first_name': first_name,
                'last_name': last_name,
                'user_name': username
            }
        )

        # Set password only for new users
        if created and password:
            user.set_password(password)
            user.save()

        return user






class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)








class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        try:
            email = attrs.get('email')
            password = attrs.get('password')

            if not email or not password:
                raise serializers.ValidationError(
                    {'credentials': 'Email and password are required'}
                )

            user = User.objects.filter(email=email).first()
            
            if not user:
                raise serializers.ValidationError(
                    {'email': 'User with this email does not exist'}
                )
                
            if not user.check_password(password):
                raise serializers.ValidationError(
                    {'password': 'Incorrect password'}
                )
                
            if not user.is_active:
                raise serializers.ValidationError(
                    {'account': 'User account is disabled'}
                )

            attrs['user'] = user  
            return attrs
            
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': str(e)})




class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()







class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField()



