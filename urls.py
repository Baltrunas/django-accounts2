from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .forms import EmailAuthenticationForm

from . import views


urlpatterns = [
	url(r'^singup/$', views.singup, name='singup'),

	url(r'^login/$',
		'django.contrib.auth.views.login',
		{
			'template_name': 'accounts/login.html',
			'extra_context': {'title': _('Login')},
			'authentication_form': EmailAuthenticationForm
		},
		name='login'
	),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^password_change/$',
		'django.contrib.auth.views.password_change',
		{
			'template_name': 'accounts/password_change.html',
			'extra_context': {'title': _('Change password')}
		},
		name='password_change'
	),
	url(r'^password_change/done/$',
		'django.contrib.auth.views.password_change_done',
		{
			'template_name': 'accounts/password_change_done.html',
			'extra_context': {'title': _('Change password')}
		},
		name='password_change_done'
	),
	url(r'^password_reset/$',
		'django.contrib.auth.views.password_reset',
		{'template_name': 'accounts/password_reset.html'},
		name='password_reset'
	),
	url(r'^password_reset/done/$',
		'django.contrib.auth.views.password_reset_done',
		{'template_name': 'accounts/password_reset_done.html'},
		name='password_reset_done'
	),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		'django.contrib.auth.views.password_reset_confirm',
		{'template_name': 'accounts/password_reset_confirm.html'},
		name='password_reset_confirm'
	),
	url(r'^reset/done/$',
		'django.contrib.auth.views.password_reset_complete',
		{'template_name': 'accounts/password_reset_complete.html'},
		name='password_reset_complete'
	),

	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/edit/$', views.edit, name='accounts_edit'),

	url(r'^bucket/$', views.bucket, name='bucket'),
	url(r'^bucket/update/$', views.bucket_update, name='bucket_update'),

	url(r'^order/$', views.order, name='order'),

	url(r'^api/xml/orders/list/$', views.orders_list, name='orders_list'),
	url(r'^api/xml/orders/update/$', views.orders_update, name='orders_update'),
	url(r'^api/xml/orders/confirm/$', views.orders_confirm, name='orders_confirm'),


	url(r'^api/json/check/$', views.json_check, name='json_check'),

	url(r'^api/json/order/list/(?P<status>new|my|history)/$', views.json_order_list, name='json_order_list'),
	url(r'^api/json/order/accept/(?P<id>[0-9]+)/$', views.json_order_accept, name='json_order_accept'),
	url(r'^api/json/order/accounting/(?P<id>[0-9]+)/$', views.json_order_accounting, name='json_order_accounting'),
	url(r'^api/json/order/status/(?P<status>processed|paid|success|canceled)/(?P<id>[0-9]+)/$', views.json_order_status, name='json_order_status'),
	# url(r'^api/json/order/update/$', views.json_order_update, name='json_order_update'),

	# url(r'^api/json/order/item/update/$id/$', views.json_order_update, name='json_order_update'),
	# url(r'^api/json/order/item/add/$', views.json_order_update, name='json_order_update'),


	# api/json/category/list/
	# api/json/category/update/
		# api/json/category/delete/

	# api/json/product/list/
	# api/json/product/update/
		# api/json/product/delete/

	# api/json/img/add/
	# api/json/img/delete/

	# 
	# api/json/orders/confirm
]