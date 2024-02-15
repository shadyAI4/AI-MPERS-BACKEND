import json
from peyha_account_utils.UserUtils import UserUtils

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .BearerTokenAuthentication import BearerTokenAuthentication



class UserVerifierView(APIView):
    authentication_classes = [BearerTokenAuthentication]
     
    def post(self, request):
        is_authenticated, user = BearerTokenAuthentication.authenticate(self,request)
        if not is_authenticated:
            return Response(data={'user': {}}, status=status.HTTP_401_UNAUTHORIZED)

        user_data = UserUtils.get_user(user)

        return Response(data={'user': json.dumps(user_data)}, status=status.HTTP_200_OK)