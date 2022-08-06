import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint
from time import sleep

class PracticeConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("Connected")

        self.socket_name = "socket_name"
        self.socket_group_name = "socket_group_name"

        # Join room group
        await self.channel_layer.group_add(
            self.socket_name,
            self.socket_group_name
        )

        await self.accept()
        await self.send(text_data={"text":"Hello from Sockets"})
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.socket_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.socket_group_name,
            {
                'type': 'message',
                'text': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))