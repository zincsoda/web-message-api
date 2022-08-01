import asyncio
import json
from channels.consumer import AsyncConsumer
from random import randint
from time import sleep

class PracticeConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connected", event)

        await self.send({"type": "websocket.accept"})
        await self.send({"type": "websocket.send", "text":"Hello from Sockets"})

    async def websocket_receive(self, event):
        print("Received", event)

        sleep(1)

        await self.send({"type": "websocket.send","text":str(randint(0,100))})

    # Receive message from room group
    async def send_message(self, event):
        print("debug 1")
        message = event['message']
        print("Sending message ", message)
        # Send message to WebSocket
        await self.send({"type": "websocket.send", "text":message})

    async def websocket_disconnect(self, event):
        print("disconnected", event)