from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from channels_permissions.consumers import Permissions
from channels_permissions.permissions import NotAnonymousUser, RequestNotAssigned, VolunteerValidated


class RequestConsumer(Permissions, JsonWebsocketConsumer):
	permission_classes = [NotAnonymousUser, RequestNotAssigned, VolunteerValidated]


	def connect(self):
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = "request%s" % self.room_name
		self.check_permissions()
		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name, self.channel_name
		)

		self.accept()

	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.room_group_name, self.channel_name
		)

	# Receive message from WebSocket
	def receive_json(self, content, **kwargs):
		message = content["message"]
		# Send message to room group
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name, {"type": "chat_message", "message": message, "user": self.scope["user"].email}
		)

	# Receive message from room group
	def chat_message(self, event):
		message = event["message"]

		# Send message to WebSocket
		self.send_json(content={"message": message, "user": event["user"]})
