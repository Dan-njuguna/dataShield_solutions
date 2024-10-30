import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MetricsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("metrics_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("metrics_group", self.channel_name)

    async def send_metrics(self, event):
        metrics = event['metrics']
        await self.send(text_data=json.dumps(metrics))