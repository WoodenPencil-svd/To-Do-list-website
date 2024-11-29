from source.use_cases.service.user import UserService
from source.use_cases.selector.user import UserSelector

from rest_framework import views, serializers , response,generics,status
from rest_framework.response import Response

from source.API.helpers import get_paginated_response, LimitOffsetPagination
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class UserListApi(views.APIView):
    http_method_names= ['get']
    class OutPutSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        username = serializers.CharField()
        
        
    class FilterSerializer(serializers.Serializer):
        username =serializers.CharField(required = False)
        
    class Pagination(LimitOffsetPagination): 
        default_limit = 10
        max_limit = 30
        # limit_query_param = 'limit'
        # limit_query_description = _('Number of results to return per page.')
        # offset_query_param = 'offset'
        # offset_query_description = _('The initial index from which to return the results.')
        # max_limit = None
        # template = 'rest_framework/pagination/numbers.html'
        
    def get(self,request,*args, **kwargs):
        filter_Serializer = self.FilterSerializer(data = request.data)
        filter_Serializer.is_valid(raise_exception= True)
        data = UserSelector.list(self,filters=filter_Serializer.validated_data)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutPutSerializer,
            queryset=data,
            request=request,
            view=self
            )

        
class UserRetrieveApi(views.APIView):
    http_method_names = ['get']
    class OutPutSerializer(serializers.Serializer):
        id  = serializers.IntegerField()
        username = serializers.CharField()
        is_active =serializers.BooleanField()
        is_staff = serializers.BooleanField()
        last_login = serializers.DateTimeField()
    
    def get(self,request,pk,*args, **kwargs):
        try:
            data = UserSelector.get_by_id(self, id = pk )
            data_serializer = self.OutPutSerializer(data).data
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data_serializer,status=status.HTTP_200_OK)
    

class UserCreateApi(views.APIView):
    http_method_names = ['post']
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()
        is_active =serializers.BooleanField()
        is_staff = serializers.BooleanField()
        
    class OutPutSerializer(serializers.Serializer):
        id  = serializers.IntegerField()
        username = serializers.CharField()
        is_active =serializers.BooleanField()
        is_staff = serializers.BooleanField()
        last_login = serializers.DateTimeField()
    
    def post(self,request,*args, **kwargs):
        try:
            input_data = self.InputSerializer(data = request.data)
            input_data.is_valid(raise_exception=True)
            user =UserService.create(self,input=input_data.validated_data)
        except Exception:
              return Response(status=status.HTTP_400_BAD_REQUEST)
          
        user_id = UserSelector.get_by_id(self,id=user.id)
        output_data = self.OutPutSerializer(user_id).data
        return Response(output_data,status=status.HTTP_201_CREATED)

        
class UserDeleteApi(generics.DestroyAPIView):
    http_method_names = ['delete']
    def delete(self,request,pk,*args, **kwargs):
        try:
            UserService.delete(self,id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)
    
class UserUpdateApi(views.APIView):
    http_method_names = ['put']
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(required = False)
        is_active =serializers.BooleanField(required = False)
        is_staff = serializers.BooleanField(required = False)
        
    class OutPutSerializer(serializers.Serializer):
        id  = serializers.IntegerField()
        username = serializers.CharField()
        is_active =serializers.BooleanField()
        is_staff = serializers.BooleanField()
        last_login = serializers.DateTimeField()
    
    def put(self,request,pk,*args, **kwargs):
        try:
            input_data = self.InputSerializer(data = request.data)
            input_data.is_valid(raise_exception=True)
            UserService.update(self,id=pk,**input_data.validated_data)
        except Exception:
              return Response(status=status.HTTP_400_BAD_REQUEST)
          
        user_id = UserSelector.get_by_id(self,id=pk)
        output_data = self.OutPutSerializer(user_id).data
        return Response(output_data,status=status.HTTP_202_ACCEPTED)

class UserLoginApi(views.APIView):
    http_method_names =['post']
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    def post(self,request):
        serializer = self.InputSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.login(self,username = serializer.validated_data['username'], password = serializer.validated_data["password"])
        if user:
            return Response(user, status=status.HTTP_200_OK)
        return Response({"Error":"Invalid username or password"},status=status.HTTP_401_UNAUTHORIZED)
    
    
