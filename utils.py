import os
import sys

import torch

dir_path = os.path.abspath('OpenVoice')
sys.path.append(dir_path)

from OpenVoice.openvoice import se_extractor
from OpenVoice.openvoice.api import ToneColorConverter


def get_tts_args(base_speaker_key, speaker_to_clone, device):
    source_embeddings = torch.load(f'checkpoints/openvoice/checkpoints_v2/base_speakers/ses/{base_speaker_key}.pth',
                                   map_location=device)

    tone_color_converter = ToneColorConverter('checkpoints/openvoice/checkpoints_v2/converter/config.json',
                                              device=device)
    tone_color_converter.load_ckpt('checkpoints/openvoice/checkpoints_v2/converter/checkpoint.pth')

    target_embeddings = se_extractor.get_se(speaker_to_clone, tone_color_converter, vad=False)[0]

    return source_embeddings, tone_color_converter, target_embeddings