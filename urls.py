from django.urls import path
from filemanage.views import FileManageView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [ path('file/',FileManageView.as_view())  ] 
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static('/media/', document_root=settings.MEDIA_ROOT)

