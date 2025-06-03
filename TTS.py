from PySide6.QtCore import QThread, Signal
import pyttsx4

""" Text-to-Speech Worker for APOLLO
    This script defines a worker class for text-to-speech conversion using the pyttsx4 library.
"""
class TTSWorker(QThread):
    finished = Signal(str)
    error = Signal(str)
    
    def __init__(self, text, voice_id=None):
        """
        Initialize the TTSWorker with text and optional voice ID.
        
        Args:
            text (str): The text to convert to speech.
            voice_id (str, optional): The ID of the voice to use. Defaults to None.
        """
        super().__init__()
        self.text = text
        self.voice_id = voice_id
        self.engine = pyttsx4.init()
        self._should_stop = False
        if self.voice_id:
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if voice.id == self.voice_id:
                    self.engine.setProperty('voice', voice.id)
                    break
        
    def run(self):
        """
        Run the TTS conversion.
        """
        try:
            self.engine.say(self.text)
            if self._should_stop:
                engine.stop()
                return
            self.engine.runAndWait()
            if self._should_stop:
                engine.stop()
                return
            self.finished.emit("Speech synthesis completed successfully.")
        except Exception as e:
            self.error.emit(e)
    
    def stop(self):
        """
        Stop the TTS conversion.
        """
        self._should_stop = True
        self.engine.stop()
        self.finished.emit("Speech synthesis stopped.")  
    
if __name__ == "__main__":
    # Example usage
    tts_worker = TTSWorker("Hello, this is a test of the text-to-speech system.")
    tts_worker.start()
    tts_worker.finished.connect(lambda msg: print(msg))
    tts_worker.error.connect(lambda err: print(err))
    tts_worker.wait()  # Wait for the thread to finish
    tts_worker.quit()  # Clean up the thread
    tts_worker.deleteLater()  # Delete the worker after use
    
    engine = pyttsx4.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")