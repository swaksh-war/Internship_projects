from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Custom_auth
from .serializers import CustomAuthSerializer

class AuthView(APIView):
    def get(self, request, user=None, auth_token = None):
        if user:
            result = Custom_auth.objects.get(user = user)
            if str(result.auth_token) == auth_token:
                return Response({'status':'verified'}, 200)
            return Response({'status': 'not verified'}, 401)
        
        return Response({'status': 'User not found'}, 404)
    
    def post(self, request):
        user = request.data.get('user')
        auth_token = request.data.get('auth_token')
        data = {'user':user, 'auth_token': auth_token}
        serializer = CustomAuthSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'user added'}, 200)
        else:
            return Response({'status':'error'}, 400)

