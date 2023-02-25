# SOLARBOT 1.0

# Author: XelXen
# License: GPL-3
# Description: A simple chatbot for telegram using AI
# Last Modified: Febuary 26, 2023

from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from config_file import name, api_id, api_hash, instruction, knowledge, bot_token
from os import environ

if name == "":
    try:
        name = environ.get("name")
    except Exception as e:
        print(e)
        print("'name' not defined")
        exit()

if api_id == "":
    try:
        api_id = environ.get("api_id")
    except Exception as e:
        print(e)
        print("'api_id' not defined")
        exit()

if api_hash == "":
    try:
        api_hash = environ.get("api_hash")
    except Exception as e:
        print(e)
        print("'api_hash' not defined")
        exit()

if instruction == "":
    try:
        instruction = environ.get("instruction")
    except Exception as e:
        print(e)
        print("'instruction' not defined")
        exit()

if knowledge == "":
    try:
        knowledge = environ.get("knowledge")
    except Exception as e:
        print(e)
        print("'knowledge' not defined")
        exit()

if bot_token == "":
    try:
        bot_token = environ.get("bot_token")
    except Exception as e:
        print(e)
        print("Running as a userbot since 'bot_token' is not defined")
        exit()

tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")

def generate(instruction, knowledge, dialog):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output

# Instruction for a chitchat task
instruction = f'Instruction: {instruction}'

knowledge = {knowledge}

if bot_token == "":
    app = Client(name=name, api_id=api_id, api_hash=api_hash)
else:
    app = Client(name=name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)

print("Bot Started!\n")

@app.on_message(filters.text & filters.private)
async def handle_generate(client, message):
    if bot_token == "":
        if message.from_user.id != client.get_me().id:
            global knowledge
            global instruction

            print("Target: " + message.text)

            dialog = [message.text]
            try:
                output  = generate(instruction, knowledge, dialog)
                await message.reply_text(output)
            except Exception as e:
                print(e)
                await message.reply_text("An error occured.")
    else:
        global knowledge
        global instruction

        print("Target: " + message.text)

        dialog = [message.text]
        try:
            output  = generate(instruction, knowledge, dialog)
            await message.reply_text(output)
        except Exception as e:
            print(e)
            await message.reply_text("An error occured.")

app.run()
