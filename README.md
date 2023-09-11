# Amgil Stun - An Educational Chatbot
 An educational chatbot created for a competetion in less than 48 hours.
 There are still many unfinished features and bugs that needs to be fixed and won't be any time soon.

## About Amgil Stun
 Amgil stun's GUI is made by using Kivy and KivyMD for its user friendly and unique interface. The AI was built with the help of tflearn, tensorflow, ntlk and numpy with the help of this [video](https://www.youtube.com/watch?v=wypVcNIH6D4). The bot uses MongoDB for cloud storage of chat history and also uses OpenAI in case the bot cannot answer the question.

## What does Amgil Stun offer?
 This chatbot was trained over physics and biology questions mainly (check model/intents.json to see all the available questions it can answer).
 Amgil Stun is not very smart yet but it works! Kind of...
 In case Amgil Stun cannot answer a question it uses OpenAI's API to get it's answer.

 Other than the AI, the app also provides a user friendly and customizable GUI, a cloud based account system where your chat history is stored and also a text to speech feature!
 An offline feature is also available.

## How to use-
 Install the pacakges by executing this command-
 ```
 pip install -r requirements.txt
 ```
 Enter your MongoDB's URI & your OpenAI's API key in [local/secerets.py](https://github.com/Krishpy-Chips/Amgil-Stun-The-Chatbot/blob/main/local/secerets.py). This is optional, if you don't specify your MongoDB's URI, the application will start in its offline mode (Note that the chat history won't be saved in offline mode).
 There are 4 AI models we have for you to use. All of them almost equally dumb.
 To use different models go to [local/data.py](https://github.com/Krishpy-Chips/Amgil-Stun-The-Chatbot/blob/main/local/data.py) and change `model_number` to a number from 0 to 3 with 3 being the smartest and 0 being the dumbest.
 In case you want to use the 0th model you will need to also change `model_epochs` to `2000`. In all models the `model_batch` will remain `8`.

## Todo list (if I ever decide to come back to this)
- Auto adjust font colour on changing theme
- Change the palette colour when changed without restart
- Enhancing the AI model's accuracy
- Expanding the AI model's dataset to answer various other subjects
- Fix window icon not showing
- Add support for Andriod & iOS
- Lag issues
- No line wrapping for long messages
