from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from project import views as project_views
from project.views import StudentUpdateView, StudentCreateView, StudentDetailView, StudentDeleteView
from account import views as account_views
from account.views import PostListView, PostDetailView, \
    UserPostListView, PostUpdateView, PostDeleteView, PostCreateView
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.userRegisterpage, name='register'),
    path('register_user/', user_views.customRegisterpage, name='register_user'),
    path('profile/', user_views.profile, name='profile'),
    path('change_account/', user_views.account, name='account'),
    path('user/<int:pk>/', user_views.dashboard, name='dashboard'),

    path('schools/', project_views.school, name='schools'),
    path('schools/<int:pk>/', project_views.departmentPage, name='departments'),
    path('departments/<int:pk>/', project_views.department_details, name='department_details'),
    path('group/<int:pk>/', project_views.singleGroup, name='single_group'),
    path('group_progress/', project_views.groupProgress, name='group_progress'),
    path('group_detail/<int:pk>', project_views.group_detail, name='group_detail'),


    path('group/<int:pk>/detail/', project_views.hodGroupDetail, name='hod_group_detail'),
    path('add_group/', project_views.create_group, name='add_group'),
    path('supervisor/<int:pk>/', project_views.hodSingle_supervisor, name='hodSingle_supervisor'),
    path('department/<int:pk>/', project_views.dean_department_detail, name='dean_department_detail'),


    # path('project/', PostListView.as_view(), name='project_home'),
    path('project/', account_views.project, name='project'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('project/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('project/new/', PostCreateView.as_view(), name='post-create'),
    path('project/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('project/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('students/new/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)