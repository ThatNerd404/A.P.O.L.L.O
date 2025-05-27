from PySide6.QtCore import QThread, Signal
from llama_cpp import Llama

class LlamaWorker(QThread):
    chunk_received = Signal(str)
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, model_path, messages, threads=6, context=0, gpu_layers=0):
        super().__init__()
        self.model_path = model_path
        self.messages = messages
        self.threads = threads
        self.context = context
        self.gpu_layers = gpu_layers
        self.stop_flag = False

    def run(self):
        try:
            llm = Llama(
                model_path=self.model_path,
                n_ctx=self.context,
                n_threads=self.threads,
                n_gpu_layers=self.gpu_layers,
                verbose=False  # Set to True for debugging
            )

            response_text = ""

            for chunk in llm.create_chat_completion(messages=self.messages, stream=True):
                if self.stop_flag:
                    break
                delta = chunk["choices"][0]["delta"].get("content", "")
                response_text += delta
                self.chunk_received.emit(delta)

            self.finished.emit(response_text)

        except Exception as e:
            self.error.emit(str(e))

    def stop(self):
        self.stop_flag = True

if __name__ == "__main__":
    # Example usage 
    llm = Llama(
                    model_path="Models\mistral-7b-instruct-v0.2-code-ft.Q4_0.gguf",
                    n_ctx= 0, # max context size, zero means use the model's default context size
                    n_threads=6,
                    n_gpu_layers=0,
                    verbose=False # makes the model print out its progress, set to True for only for debugging
                )

    response_text = ""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    for chunk in llm.create_chat_completion(messages=messages, stream=True):
        delta = chunk["choices"][0]["delta"].get("content", "")
        response_text += delta
        print(delta, end='', flush=True)
