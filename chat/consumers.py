from asgiref.sync import async_to_sync

from channels_permissions.consumers import PermissionsJsonWebsocketConsumer
from channels_permissions.permissions import *
from chat.models import Message
from chat.serializers import MessageSerializer


class ChatRoomConsumer(PermissionsJsonWebsocketConsumer):
	permission_classes = [CanAccessChatRoom]
	room = None
	user = None

	def connect(self):
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = "chat_room%s" % self.room_name
		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name, self.channel_name
		)

		self.accept()
		self.room = get_chat_room(int(self.room_name))
		self.user = self.scope['user']

	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.room_group_name, self.channel_name
		)

	# Receive message from WebSocket
	def receive_json(self, content, **kwargs):

		data = content["data"]
		message = create_message(self.user, self.room, data["message"])
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name, {"type": "chat_message", "message": serialize_message(message)}
		)

	# Receive message from room group
	def chat_message(self, event):
		message = event["message"]

		# Send message to WebSocket
		self.send_json(content={"data": message})


def create_message(user, room, message) -> Message:
	return Message.objects.create(author=user, room=room, message=message)


def serialize_message(message) -> dict:
	return MessageSerializer(message).data
