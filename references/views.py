#coding: utf-8
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import pagination
from rest_framework.parsers import FileUploadParser

from .models import ReferencesModel, GroupReferencesModel, TzModel, SPGZKPGZModel, EstimateModel
from .serializers import GroupRefSerializer, RefSerializer, FileSerializer, TZSerializer, SPGZSerializer, EstimateSerializer
from rest_framework import filters
from django_filters import rest_framework


class ListGroupDocumentApiView(generics.ListCreateAPIView):
    """
    get: Получение списка видов справочников

    post: Добавление вида справочника
    """
    queryset = GroupReferencesModel.objects.all().order_by('id')
    serializer_class = GroupRefSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_fields = ['id']


class UpdateGroupDocumentApiView(generics.UpdateAPIView):
    """
        patch: Частичное обновление вида справочника по id

        put: Обновление вида справочника по id
        """
    queryset = GroupReferencesModel.objects.all()
    serializer_class = GroupRefSerializer


class DeleteGroupDocumentApiView(generics.DestroyAPIView):
    """
        delete: Удаление вида справочника
        """
    queryset = GroupReferencesModel.objects.all()
    serializer_class = GroupRefSerializer


class ListReferencesApiView(generics.ListCreateAPIView):
    """
        get: Получение списка записей в справочнике СН/ТСН

        post: Добавление записи в справочник СН/ТСН
        """
    queryset = ReferencesModel.objects.all().order_by('id')
    serializer_class = RefSerializer
    pagination = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['name_works_and_costs']
    filterset_fields = ['document']


class UpdateReferencesApiView(generics.UpdateAPIView):
    """
        put: Обновление справочника СН/ТСН по id

        patch: Частичное обновление справочника СН/ТСН по id
        """
    queryset = ReferencesModel.objects.all()
    serializer_class = RefSerializer


class DeleteReferencesApiView(generics.DestroyAPIView):
    """
        delete: Удаление записи из справочника СН/ТСН
        """
    queryset = ReferencesModel.objects.all()
    serializer_class = RefSerializer


class ListTZApiView(generics.ListCreateAPIView):
    """
        get: Список справочника ТЗ

        post: Добавление записи в справочник ТЗ
        """
    queryset = TzModel.objects.all().order_by('id')
    serializer_class = TZSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'kpgz', 'spgz']
    filterset_fields = ['id', 'document_id']


class UpdateTZApiView(generics.UpdateAPIView):
    """
        put: Обновление справочника ТЗ по id

        patch: Частичное обновление справочника ТЗ по id
        """
    queryset = TzModel.objects.all()
    serializer_class = TZSerializer


class DeleteTZApiView(generics.DestroyAPIView):
    """
        delete: Удаление справочника ТЗ по id
        """
    queryset = TzModel.objects.all()
    serializer_class = TZSerializer


class ListSPGZApiView(generics.ListCreateAPIView):
    """
        get: Список справочника СПГЗ/КПГЗ

        post: Добавление записи в справочник СПГЗ/КПГЗ
        """
    queryset = SPGZKPGZModel.objects.all().order_by('id')
    serializer_class = SPGZSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['kpgz', 'spgz']
    filterset_fields = ['id', 'document_id']


class UpdateSPGZApiView(generics.UpdateAPIView):
    """
        put: Обновление справочника СПГЗ/КПГЗ по id

        patch: Частичное обновление справочника СПГЗ/КПГЗ по id
        """
    queryset = SPGZKPGZModel.objects.all()
    serializer_class = SPGZSerializer


class DeleteSPGZApiView(generics.DestroyAPIView):
    """
        delete: Удаление сперавочника СПГЗ/КПГЗ по id
        """
    queryset = SPGZKPGZModel.objects.all()
    serializer_class = SPGZSerializer


class ListEstimateApiView(generics.ListCreateAPIView):
    """
        get: Вывод разобранной сметы

        post: Добавление записи в разообранные сметы
        """
    queryset = EstimateModel.objects.all().order_by('id')
    serializer_class = EstimateSerializer
    pagination = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend]
    search_fields = ['name_works_and_costs']
    filterset_fields = ['id']


class UpdateEstimateApiView(generics.UpdateAPIView):
    """
        put: Обновление сметы по id

        patch: Частичное обновление сметы по id
        """
    queryset = EstimateModel.objects.all()
    serializer_class = EstimateSerializer


class DeleteEstimateApiView(generics.DestroyAPIView):
    """
        delete: Удаление разобранной сметы по id
    """
    queryset = EstimateModel.objects.all()
    serializer_class = EstimateSerializer


class FileUploadView(generics.GenericAPIView):
    """
        post: Загрузка файла, в проекте пока не используется
        """
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)