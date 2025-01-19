#projects 
 **A**utomated **P**ersonalized **O**perations for **L**earning and **L**ife **O**rganization. APOLLO  will take in equations and solve them for you like a calculator.  I need to have a basis of numpy, pandas and matplotlib so I will start learning those first. REMEMBER USE PIP IN POWERSHELL python -m pip install thepackage. A stepping stone in my quest to go into [[AI Development]]. This is the different animations I have made to turn apollo into a desktop pet. This allows him to always be around but unobtrusive.
 Idle Animation:
![[Apollo_Idle.gif]]
Loading Animation:
![[Apollo_Loading.gif]]

## Goals for phase 1
- [x] Make sure to keep the project organized (pythonic with classes and such)
- [x] now take audio input with `SpeechRecognition`
- [x] Now make it answer with voice with `pyttsx3` 
## Goals for phase 2
- [x] remove redundant code and do some error handling
- [x] Add basic chatbot functionality
## Goals for phase 3
- [x] create an ollama llm on computer
- [x] finetune said llm to give it a personality and train it on some obisdian notes (don't do that and use prompt and context engineering because its way cheaper)
- [x] figure out how to grab the data from the local host thing? (figure out I don't need that at all and just use langchain)
## Goals for phase 4
- [x] implement RAG
- [x] organize a bit better and possible switch stuff to being in a bunch of files and make more pythonic
# After phase 4 take break to chill and just focus more on pixel art and website!

## Goals for phase 5
- [ ] more prompt engineering
- [ ] more bug fixing 
- [ ] add more documents to load (pep 8 docs so I can always have my code be formatted )
## Goals for phase 6
- [ ] give it an activation phrase and background listening 
- [ ] figure out threading programming and see if that can help with optimizing the speed of the program
- [ ] try to see if I can change the voice to sumn else
## Goals for phase 7
- [ ] add new commands to let it do certain tasks like:
	- [ ] play music
	- [ ] take notes
	- [ ] set alarms / reminders
## Goals for final phase
- [ ] combine with desktop pet and deploy on computer
- [ ] optimize speed better

## To-do List:
- [x] Figure out langchain
- [ ] Read "Langchain in Action"
- [ ] read this https://realpython.com/async-io-python/
- [ ] make relevant document score thing go with range of 0-1 not 0-infinity
- [ ] take score to make it not grab documents if below a certain relevance threshold
- [ ] turn `get_relevant_documents():` into a part of the chain invoking thing maybe?
- [ ] look into the different libraries that I will need for the project
	- [x] `SpeechRecognition` for speech recognintion,
	- [x] `spaCy`, `NLTK`, or pre-trained models like OpenAI's GPT (via transformers) for natural language processing,
	- [x] `pyttsx3` for text to speech / TTS
	- [ ] Ollama python library
	- [x] Langchain
	- [ ] PyDub and playsound for playing music
- [x] increase microphone sensitivity
- [x] figure out weird error where if I say any of the deactivation words it bugs out and I have to say it twice
- [x] Watch tutorial on transformers and figure out how that shit works
- [x] look up wtf the whisper thing is to see if it works better than the SpeechRecognition library (look into getting a different speech recognizer to work without internet)
- [x] change from google audio to whisper ai for offline stuff
- [x] switch to whisper for better accuracy and speed while still being offline
	- [x] install pytorch (current latest is python version is 3.13.0 so we downgraded to 3.10.0)
	- [x] install whisper ai
- [ ] wait for pytorch support 3.13.0 to drop so I can move update everything to 3.13.0 (remember you change it via the bottom right thing)
