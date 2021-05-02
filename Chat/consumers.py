from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    """
        This Consumer for Chat Model
    """
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.accept()


    def disconnect(self, code):
        pass

    def receive(self, text_data):
        text_data_dict = json.loads(text_data)
        message = text_data_dict['message']

        self.send(text_data=json.dumps({
            'message':message
        }))