from django.urls import path, include
from Appyhouselist_app.api.views import GetCommentsPerUser, PropertyListAV, PropertyDetailAV, CompanyListAV, CompanyDetailAV, CommentDetail, commentsList, commentsAll, commentsCreate, CompanyVS, PropertyList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('company', CompanyVS, basename = 'company')

urlpatterns = [
    path('property/',PropertyListAV.as_view(), name='property'),
    path('property/list/',PropertyList.as_view(), name='property-list'),
    path('property/<int:pk>',PropertyDetailAV.as_view(), name='property-detail'),
    path('', include(router.urls)),
    #path('company/',CompanyListAV.as_view(), name='company'),
    #path('company/<int:pk>',CompanyDetailAV.as_view(), name='company-detail'),
    path('property/comment/',commentsAll.as_view(), name='comment-list'),
    path('property/<int:pk>/comment-create/',commentsCreate.as_view(), name='comment-create'),
    path('property/<int:pk>/comment/',commentsList.as_view(), name='comment-list'),
    path('property/comment/<int:pk>',CommentDetail.as_view(), name='comment-detail'),
    #path('property/comments/<str:username>', GetCommentsPerUser.as_view(), name='comments-per-user'),
    path('property/comments/', GetCommentsPerUser.as_view(), name='comments-per-user'),

]

