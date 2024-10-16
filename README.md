# base-telegram-bot

###
### Telgram bot based on OpenAI
### 

This is an example of a base conversational telegram bot with openAI gpt-4.
###

### Prerequisites
1. Create a telegram bot using [@BotFather](https://telegram.me/BotFather) and save the token;
2. Create a openAI api key:
   1. Login https://platform.openai.com/docs/overview and go to your profile
   2. Select `User API Keys`
   3. Click on `Create new secret key` and save it
3. Create a `.env` file starting from `example.env` filling the placeholders with
your data
4. [Optional] Create a virtual environment
    
        python3.11 -m venv venv
        source venv/bin/activate

5. Install requirements
    
        pip install -r requirements.txt

###
### Run
Run the bot with 

    python bot.py


