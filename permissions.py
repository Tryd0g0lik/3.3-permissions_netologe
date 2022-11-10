from rest_framework.permissions import BasePermission


class OwnerPermissions(BasePermission): #ограничение прав
	def has_object_permission(self, request, view, obj):
		if request.method == 'GET':
			return True
		return request.user == obj.user