from django.conf.urls import url
from . import views

urlpatterns = [
    # /stock_order/
    url(r'^$', views.index, name='index'),

    # /stock_order/rtc_unit
    url(r'^rtc_unit/', views.rtc_unit, name='rtc_unit'),

    # /stock_order/prep 1
    url(r'^prep_1/', views.prep_1, name='prep_1'),

    #/stock_order/deletequeueitem
    url(r'deletequeueitem/', views.deleteFromWashQueue, name='deleteQueueItem')

]


