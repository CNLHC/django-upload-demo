from django.urls import path
from filemanage.views import FileManageView

urlpatterns = [
        path('file/',FileManageView.as_view()),

]
