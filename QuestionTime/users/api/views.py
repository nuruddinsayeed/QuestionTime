from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer

class CurrentUserAPIView(APIView):
    """Manages get request to our api endpoint"""

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)