from django.urls import path
from references import views

app_name = 'sndirectory'

urlpatterns = [
    #url для работы со справочниками, именно название справочника, название группы
    path('directory_list/', views.ListGroupDocumentApiView.as_view()),
    path('directory_list/update/<int:pk>', views.UpdateGroupDocumentApiView.as_view()),
    path('directory_list/delete/<int:pk>', views.DeleteGroupDocumentApiView.as_view()),
    #url подробные данные справочника
    path('directory/', views.ListReferencesApiView.as_view()),
    path('directory/update/<int:pk>', views.UpdateReferencesApiView.as_view()),
    path('directory/delete/<int:pk>', views.DeleteReferencesApiView.as_view()),
    #
    path('upload/', views.FileUploadView.as_view(), name='files'),
    #Справочник ТЗ
    path('tz/', views.ListTZApiView.as_view()),
    path('tz/update/<int:pk>', views.UpdateTZApiView.as_view()),
    path('tz/delete/<int:pk>', views.DeleteTZApiView.as_view()),
    #
    path('spgz/', views.ListSPGZApiView.as_view()),
    path('spgz/update/<int:pk>', views.UpdateSPGZApiView.as_view()),
    path('spgz/delete/<int:pk>', views.DeleteSPGZApiView.as_view()),
    #
    path('estimate/', views.ListEstimateApiView.as_view()),
    path('estimate/update/<int:pk>', views.UpdateEstimateApiView.as_view()),
    path('estimate/delete/<int:pk>', views.DeleteEstimateApiView.as_view()),
]