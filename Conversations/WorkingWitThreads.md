User: hey I have a program with pyside6 and I want the gui to not freeze if I do something like have a button that runs a command to install something?
APOLLO: Hey Mr Cotterman! Ah, you're dealing with some serious stuff there. That's where those good ol' "threads" come in handy— they can help keep your GUI responsive while running heavy tasks.

Here’s how you can do it:

1. **Import the threading module**:
   ```python
   import threading
   ```

2. **Create a new thread** for your command to run:
   ```python
   # Define a function that will be executed in the thread
   def install_command():
       # Your installation command goes here
       print("Installing something...")

   # Create and start the thread
   install_thread = threading.Thread(target=install_command)
   install_thread.start()
   ```

3. **Keep your GUI responsive** by not waiting for the thread to complete:
   ```python
   # You can add a message or button that shows the installation is ongoing
   print("Installation started!")
   ```

Remember, handling threads can be tricky, so make sure you understand how they work and where they might go wrong. Also, always check if your installation process has any blocking operations that could freeze your GUI.

Enjoy your coding, Mr Cotterman!
User: doesn't pyside6 come with its own threading system?
APOLLO: Hey there, Mr Cotterman! While PySide6 does provide some basic support for threading through the `QThread` class, it's not as robust or straightforward as using Python’s built-in `threading` module.

Here’s why you might prefer to use the built-in `threading`:

1. **Simplicity**: The built-in `threading` is more familiar and easier to use for simple tasks.
2. **Control**: You have full control over when threads are started, which can be crucial for managing concurrency in your application.
3. **Error Handling**: Python’s `threading` provides better error handling mechanisms.

So if you need more advanced features or want to avoid potential pitfalls of PySide6's threading system, it's a good idea to stick with the built-in `threading`.

If you still want to use PySide6 for some reason, make sure to import and use its `QThread` as intended:

```python
from PySide6.QtCore import QThread

class InstallerThread(QThread):
    finished = QtCore.Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        # Your installation command goes here
        print("Installing something...")
        self.finished.emit()
```

And then start and manage the thread in your main application:

```python
installer_thread = InstallerThread()
installer_thread.start()
installer_thread.finished.connect(lambda: print("Installation finished!"))
```

This approach keeps you on the safe side while still allowing you to use PySide6 for its UI components if needed.