from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
import pytz

@api_view(["GET"])
@permission_classes([AllowAny])
def server_time(request):
    india_tz = pytz.timezone('Asia/Kolkata')
    now = timezone.now().astimezone(india_tz)
    return Response({
        "server_time": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "timezone": "Asia/Kolkata"
    })