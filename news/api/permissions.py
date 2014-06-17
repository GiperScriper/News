# -*- coding: utf-8 -*-

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		#Allow all read type requests
 		if request.method in permissions.SAFE_METHODS:
			return True

		#this leaves us with write requests (i.e. POST / PUT / DELETE)
		return obj.moderator == request.user