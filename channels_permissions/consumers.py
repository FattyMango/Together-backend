import logging
from channels.exceptions import DenyConnection
from .permissions import BasePermission

logger = logging.getLogger(__name__)
class Permissions(object):
	permission_classes = [BasePermission]

	def check_permissions(self):
		try:
			for permission in self.permission_classes:
				if permission(scope=self.scope).validate() != None:
					# logger.error(type(permission(scope=self.scope)))
					raise DenyConnection
		except PermissionError:
			raise DenyConnection


