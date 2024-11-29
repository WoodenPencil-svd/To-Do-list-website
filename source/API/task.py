from rest_framework import serializers , views , status
from rest_framework.response import Response

from source.use_cases.selector.task import TaskSelector
from source.use_cases.service.task import TaskService


from source.API.helpers import get_paginated_response, LimitOffsetPagination
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

class TaskListApi(views.APIView):
    http_method_names = ['get']
    
    class Pagination(LimitOffsetPagination): 
        default_limit = 10
        max_limit = 30
        # limit_query_param = 'limit'
        # limit_query_description = _('Number of results to return per page.')
        # offset_query_param = 'offset'
        # offset_query_description = _('The initial index from which to return the results.')
        # max_limit = None
        # template = 'rest_framework/pagination/numbers.html'
    
    class OutPutSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        
    class FilterSerializer(serializers.Serializer):
        title = serializers.CharField(required = False)
    
    def get(self,request,*args, **kwargs,):
        filter = self.FilterSerializer(data = request.data)
        filter.is_valid(raise_exception=True)
        data = TaskSelector.list(self, filters=filter.validated_data)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutPutSerializer,
            queryset=data,
            request=request,
            view=self
            )
        
    
class TaskRetrieveApi(views.APIView):
    http_method_names = ['get']
    class OutPutSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user =  serializers.CharField()
        status = serializers.CharField()
    def get(self,request,pk,*args, **kwargs):
        try:
            data = TaskSelector.get_by_id(self,id=pk)
            output = self.OutPutSerializer(data).data
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(output,status=status.HTTP_202_ACCEPTED)
    
        
class TaskCreateApi(views.APIView):
    http_method_names = ['post']
    class OutPutSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user =  serializers.CharField()
        status = serializers.CharField() 
        
    class InPutSerializer(serializers.Serializer):
        title = serializers.CharField()
        user_id =  serializers.IntegerField()
        
    def post(self,request,*args, **kwargs):
        input = self.InPutSerializer(data= request.data)
        input.is_valid(raise_exception=True)
        try:
            task = TaskService.create(self,input=input.validated_data)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        task_id = TaskSelector.get_by_id(self,id=task.id)
        task_data = self.OutPutSerializer(task_id).data
        return Response(task_data,status=status.HTTP_201_CREATED)
        
        
class TaskUpdateApi(views.APIView):
    http_method_names = ['put']
    class OutPutSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        user =  serializers.CharField()
        status = serializers.CharField() 
        
    class InPutSerializer(serializers.Serializer):
        title = serializers.CharField(required =False)
        user_id =  serializers.IntegerField(required =False)
    
    def put(self,request,pk,*args, **kwargs):
        input = self.InPutSerializer(data= request.data)
        input.is_valid(raise_exception=True)
        try:
           TaskService.update(self,id=pk,**input.validated_data)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        task_id = TaskSelector.get_by_id(self,id=pk)
        task_data = self.OutPutSerializer(task_id).data
        return Response(task_data,status=status.HTTP_200_OK)
        
    
class TaskDeleteApi(views.APIView):
    http_method_names = ['delete']
    def delete(self,request,pk,*args, **kwargs):
        try:
            TaskService.delete(self,id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)
        
