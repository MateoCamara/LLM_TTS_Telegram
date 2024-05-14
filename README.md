
# Building an LLM+TTS Assistant on Telegram with Open Source Technology

Welcome to the GitHub repository for the Mindsait conference presentation titled "Building an LLM+TTS Assistant on Telegram with Open Source Technology" by Mateo Cámara, held on May 14, 2024. This repository contains all the necessary materials to set up your Telegram bot using open-source tools. If you find this useful, please consider giving us a star!

## Getting Started

### Step 1: Clone This Repository

Start by cloning this repository to your local machine:

```bash
git clone <repository-url>
```

### Step 2: Clone OpenVoice Repository

Inside the root directory of this repository, clone the OpenVoice repository:

```bash
git clone git@github.com:myshell-ai/OpenVoice.git
```

Additionally, download the original voice model weights trained with OpenVoice from the following link:

[Download Voice Weights](https://myshell-public-repo-hosting.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip)

Unzip them and store them in checkpoints/openvoice

### Step 3: Install Requirements

To install all necessary libraries, run:

```bash
pip install -r requirements.txt
```

If you are using a GPU, visit [PyTorch Official Site](https://pytorch.org/get-started/locally/) to install the correct version of PyTorch for your CUDA version.

### Step 4: Download Language Dictionary

The OpenVoice version used requires a specific language dictionary. Download it with:

```bash
python -m unidic download
```

### Step 5: Download oLlama

Download oLlama from:

[Download oLlama](https://ollama.com/)

Important: Before running the code, start the oLlama program to ensure a language model server is running.

### Step 6: Setup Your Voice

Store a high-quality voice recording in the `resources` directory and reference it in the `setup_tts` function in the code.

### Step 7: Create Your Telegram Bot

Follow this comprehensive guide to create your Telegram bot:

[Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial)

Store your Telegram bot token in a `.env` file to keep it secure but accessible to your application.

### Step 8: Run the code!

Run the code with:

```bash
python main.py
```

Now you should be able to talk to your Telegram bot!

## Contributing

Feel free to fork this repository, make changes, and submit pull requests if you have improvements or suggestions. Contributions are welcome!

## Acknowledgments

- Mindsait Conference
- Myshell AI for OpenVoice
- oLlama team
