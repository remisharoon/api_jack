from django.contrib.auth.models import User
from django.http import Http404
from .serializers import UserInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo
from os import listdir
from os.path import isfile, join
from django.db import connection
import copy
class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        print request.GET
        query_attributes = {}
        if len(request.GET) > 0:
            query_attributes = dict([(param, val) for param, val in request.GET.iteritems() ])
    
        print query_attributes
        user_info = UserInfo.objects.all().filter(**query_attributes)
        serializer = UserInfoSerializer(user_info, many=True)
        
        res = list()
        for rec in serializer.data:
            d = copy.deepcopy(rec)
            res_dict = copy.deepcopy(d['user'])
            del d['user']
            del d['id']
            res_dict.update(d)
            res.append(res_dict)
        return Response(res)


class FilesList(APIView):
    """
    Retrieve a list of files in directory
    """
    def get(self, request, format=None):
        if 'fpath' in request.GET:
            fpath = request.GET['fpath']
            try:
                files_list = [ f for f in listdir(fpath) if isfile(join(fpath,f)) ]
            except Exception as e:
                return Response(str(e))
            return Response(files_list)
        else:
            return Response("provide filepath as url parameter")

class SystemStatus(APIView):
    """
    Retrieve status of system componets
    """
    def get(self, request, format=None):
        try:
            Response(connection.queries)
            stat = status.HTTP_200_OK
        except Exception as e:
            stat = status.HTTP_503_SERVICE_UNAVAILABLE
        return Response({'mysql_status':stat})
