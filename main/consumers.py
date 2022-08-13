import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint
from time import sleep
from channels.layers import get_channel_layer

class PracticeConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.channel_group_name = "channel_group_name"

        print("Connected to ", self.channel_name)
        # Join room group
        await self.channel_layer.group_add(
            self.channel_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data="Hello sockets!")
        
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.channel_group_name,
            {
                'type': 'message',
                'text': message
            }
        )

    async def notify(self, event):
        """
        This handles calls elsewhere in this codebase that look
        like:

            channel_layer.group_send(group_name, {
                'type': 'notify',  # This routes it to this handler.
                'content': json_message,
            })

        Don't try to directly use send_json or anything; this
        decoupling will help you as things grow.
        """
        print("notify")
        await self.send(event["content"])
