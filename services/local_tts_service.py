# services/local_tts_service.py
import coqui

class LocalTTSService:
    def __init__(self):
        self.model = coqui.TTS(models=["tts_models/en/ljspeech/tacotron2-DDC"])
        self.callbacks = {'speech': []}

    async def generate(self, llm_reply, icount):
        audio_path = self.model.tts_to_file(text=llm_reply["partialResponse"], file_path=f"output_{icount}.wav")
        with open(audio_path, "rb") as f:
            audio = f.read()
        await self._trigger('speech', icount, audio, llm_reply["partialResponse"])

    def on(self, event: str, callback):
        if event in self.callbacks:
            self.callbacks[event].append(callback)

    async def _trigger(self, event: str, *args):
        for callback in self.callbacks[event]:
            await callback(*args)
