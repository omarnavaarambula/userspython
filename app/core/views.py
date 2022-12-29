from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UploadSerializer, UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import datetime
import jwt


class StatusView(APIView):
    
    def get(self, request):
        return Response({'result':'Server is running and ok'}, status=status.HTTP_200_OK)
    
class FileUploadView(APIView):
    
    serializer_class = UploadSerializer

    def get(self, request):
        return Response("Hi")
    
    def post(self, request):
        file_upload = request.FILES.get('file_upload')
        f = file_upload.open()
        content_type = file_upload.content_type
        response = {
            'result':'file upload successfully', 
            'content_type':content_type,
            'value': f.read()}
        
        return Response(response, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def hello_world(request):
        
    if request.method == 'POST':
        return Response ({"message": "got some data", "data":request.data})
    return Response ({'message': 'hello world'})


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
class LoginView(APIView):
    
    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
        }

        return response
    
class UserView(APIView):
    
    def get(self, request):
        
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
    
        return Response(serializer.data)
    
class LogoutView(APIView):
    
    def post(self, request):
        
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'sucessfull logout'
        }

        return response