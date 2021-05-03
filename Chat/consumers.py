from channels.generic.websocket import WebsocketConsumer
import json
from tkinter import *



class ChatConsumer(WebsocketConsumer):
    """
        This Consumer for Chat Model
    """

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'caht_{self.room_name}'

        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_dict = json.loads(text_data)
        message = text_data_dict['message']


        self.channel_layer.group_send (
            self.room_group_name,
            {
                'type': None,
                'message': message,
            }
        )
    def chat_message(self, event):

        self.send(text_data=json.dumps({
            'message': message
        }))
