# Conversation Assistant (APOLLO)

This repository contains an AI-powered conversation assistant that can adapt to various personas and assist with different types of interactions. The tool supports saving and loading conversations for future use. A.P.O.L.L.O or Automated Personal Operation for Life, Learning, and Organization is a software application with a whimiscal GUI and a very customizable experience. Putting the power of AI into your control! This is my first public project so be wary!


## Features

- **Adaptive Personas**: APOLLO adapts its responses based on the selected persona.
  - Standard Assistance
  - Socratic Tutor (Socratic Persona)
  - Gritty Punk Assistant
  
- **Save/Load Functionality**:
  - Saves current conversation display and history into a .md file for later access or sharing with others.

## Usage Instructions

### Initial Setup:
1. Install Ollama from their website [here](https://ollama.com/)**
2. Install the default models: phi4-mini and qwen2.5-coder:3b with `Ollama pull model-name` in your terminal
3. Clone the repository.
4. run `pip install -r requirements.txt` 
5. Run APOLLO by executing `python main.pyw`.
6. (Optional) Install pyshortcuts and create a shortcut for the main.pyw file

### Interacting With The Assistant:
To begin a new session, type your initial prompt in the textbox and either click enter or use the submit button.
To refresh the conversation click the refresh button or use the `Crtl+R` shortcut.

#### Example Sessions:

1. **Standard Assistance**: 
    - User Input ("Sir Cotterman"): "Tell me about climate change."
    - APOLLO Output: Initial explanation
    ![Default APOLLO gif](https://github.com/ThatNerd404/A.P.O.L.L.O/blob/main/Assets/Apollo_Idle.gif)
2. **Socratic Tutor Persona**
    - User Input ("Sir Cotterman): "Explain quantum mechanics in detail."
    - Initial Explanation, Sources for further research, and Follow-up Questions
    ![Tutor APOLLO gif](https://github.com/ThatNerd404/A.P.O.L.L.O/blob/main/Assets/Apollo_Idle_Tutoring.gif)
3. **Gritty Punk Coding Assistant** 
   - User Input ("Mr Cotterman"): "What's up Choom?"
   - Grumpy yet helpful responses with references to cyberpunk and examples.
    ![Coding APOLLO gif](https://github.com/ThatNerd404/A.P.O.L.L.O/blob/main/Assets/Apollo_Idle_Coding.gif)
### Saving Conversations:

To save your session into files for later use:
1. Click the save button or use the "Crtl+S" shortcut.
2. Enter your filename and remember to put it in a format that works for files.

The conversation will be saved as both `.md` (Markdown) display history, and corresponding text (`*.txt`) containing JSON-serialized convo history.

### Loading Saved Conversations:

To load an existing session:
1. Run APOLLO.
2. Choose a file.
3. The app will open the file and load the conversation to the model and the display history to the display. (in `/Conversations` directory).

## Troubleshooting

If you encounter issues, check for any error messages in the logs and refer back to this README for troubleshooting tips.

**Please report bugs using GitHub Issues at [here](https://github.com/ThatNerd404/A.P.O.L.L.O/issues)**

*Note: This application is intended strictly as a conversation assistant; it cannot replace professional advice or services.*

Happy Conversing!
