import jwt
from rest_framework import serializers
from .models import Register, Article
from rest_framework import exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'username', 'email', 'password', 'gender']
        extra_kwargs = {  # extra kwargs which is used for hide sensitive data field from deserialization
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.get('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # instance.set_password(password)
            instance.save()
            return instance


# class BlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

#     def create(self, validated_data):
#         master = Article.objects.create(**validated_data)
#         return master


"""class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            if auth_header:
                token = auth_header.split(' ')[1]
                id = token['id']
                print(id)
                # do something with the token here
                ...
        master = Article.objects.create(id=id, **validated_data)
        return master
"""


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        print("request values", request)
        print("request value", request)
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        # checking header value
        print("token", type(auth_header))

        if auth_header:
            # Get the token string from the auth header
            token_string = auth_header
            print(token_string)
            decoded_token = jwt.decode(
                token_string, 'secret', algorithms=['HS256'])
            """try:
                # Decode the token using the secret key
                decoded_token = jwt.decode(
                    token_string, 'secret_key', algorithms=['HS256'])
                print(decoded_token)
            except jwt.exceptions.DecodeError:
                raise exceptions.AuthenticationFailed('Invalid token')"""

            # Extract the id field from the decoded token
            id = decoded_token.get('id')
            print("id", id)

            # Use the id field in the creation of the Article object
            master = Article.objects.create(ids=id, **validated_data)
            return master
