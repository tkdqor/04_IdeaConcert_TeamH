from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# url : GET api/v1/bossRaid
class HelloAPIView(APIView):
    """
    Assignee : 훈희
    Hello message를 내보내는 api view 입니다.
    """

    def get(self, request):

        return Response({"Hello"}, status=status.HTTP_200_OK)
