# %% IMPORTS ##

import os
import sys
import torch
from dotenv import load_dotenv

from utils import get_tts_args

dir_path = os.path.abspath('OpenVoice')
sys.path.append(dir_path)

from langchain_community.llms import Ollama

from melo.api import TTS

from telegram.ext import Updater, CommandHandler

# %% ENVIRONMENT VARIABLES ##

load_dotenv()
device = "cuda:0" if torch.cuda.is_available() else "cpu"
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ALLOWED_USER_ID = os.getenv('ALLOWED_USER_ID')


# %% LLM ##

def setup_llm():
    # We need to instantiate the LLM model.
    llm = Ollama(model="gemma", device=device)

    return llm


def generate_text(llm, input):
    # We need to generate text using the LLM model.
    response = llm.invoke(input,
                          max_length=30,
                          num_return_sequences=1)
    return response


# %% TTS ##

def setup_tts(speaker_to_clone):
    # The TTS model we are going to use is the OpenVoice TTS model.
    # We need to instantiate the TTS model.
    tts_model = TTS(language="EN_NEWEST", device=device)

    base_speaker_key = 'en-br'

    # We need to get the speaker embeddings for the speaker we want to clone
    # and the speaker we want to clone from. We also need to instantiate the
    # tone color converter.
    source_embeddings, tone_color_converter, target_embeddings = get_tts_args(base_speaker_key,
                                                                              speaker_to_clone,
                                                                              device)

    return tts_model, source_embeddings, tone_color_converter, target_embeddings


def text2speech(text, tts_model, source_embeddings, tone_color_converter, target_embeddings):
    output_dir = 'outputs_openvoice'
    src_path = f'{output_dir}/tmp.wav'
    save_path = f'{output_dir}/output.wav'

    speed = 1.0
    speaker_id = 0

    # We need to convert the text to speech using the TTS model.
    # It will save the temp audio file in the src_path.
    tts_model.tts_to_file(text,
                          speaker_id,
                          src_path,
                          speed=speed)

    # We need to convert the tone and color of the audio file using the tone color converter.
    # It will save the converted audio file in the save_path.
    tone_color_converter.convert(
        audio_src_path=src_path,
        src_se=source_embeddings,
        tgt_se=target_embeddings,
        output_path=save_path)

    return save_path


# %% TELEGRAM ##

def setup_telegram():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("mateo", pipeline))

    updater.start_polling()

    return updater


# %% PIPELINE ##

def pipeline(update, context):
    print('mensaje recibido')

    text = ' '.join(context.args)
    response = generate_text(llm, text)
    update.message.reply_text(response)
    text2speech(response, *tts_args)

    with open("outputs_openvoice/output.wav", 'rb') as audio_file:
        update.effective_message.reply_audio(audio=audio_file)


# %% MAIN ##

if __name__ == '__main__':
    llm = setup_llm()
    tts_args = setup_tts("resources/mateo_record.wav")
    telegram = setup_telegram()

    print('Bot is running...')

    telegram.idle()
