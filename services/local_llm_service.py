# services/local_llm_service.py
from transformers import pipeline

class LocalLLMService:
    def __init__(self):
        self.model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
        self.callbacks = {'llmreply': []}

    async def completion(self, text, interaction_count):
        response = self.model(text, max_length=150)
        reply = response[0]["generated_text"]
        await self._trigger('llmreply', {"partialResponse": reply}, interaction_count)

    def on(self, event: str, callback):
        if event in self.callbacks:
            self.callbacks[event].append(callback)

    async def _trigger(self, event: str, *args):
        for callback in self.callbacks[event]:
            await callback(*args)
