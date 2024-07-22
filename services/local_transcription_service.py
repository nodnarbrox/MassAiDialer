# services/local_transcription_service.py
import whisper

class LocalTranscriptionService:
    def __init__(self):
        self.model = whisper.load_model("base")
        self.callbacks = {'utterance': [], 'transcription': []}

    async def connect(self):
        pass

    async def disconnect(self):
        pass

    def on(self, event: str, callback):
        if event in self.callbacks:
            self.callbacks[event].append(callback)

    async def send(self, audio_data: bytes):
        result = self.model.transcribe(audio_data)
        transcription = result["text"]
        await self._trigger('transcription', transcription)

    async def _trigger(self, event: str, *args):
        for callback in self.callbacks[event]:
            await callback(*args)
