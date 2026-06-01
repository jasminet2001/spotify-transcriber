# spotify-transcriber
A simple Spotify Transcriber
# Spotify Podcast Transcriber

A simple Python tool that transcribes podcast episodes using Faster-Whisper.

## Prerequisites

* Python 3.10+
* FFmpeg
* Faster-Whisper

## Installation

Clone the repository:

```bash
git clone https://github.com/jasminet2001/spotify-transcriber.git
cd spotify-podcast-transcriber
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg:

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Downloading the Podcast Audio

This project currently requires the podcast audio file to be downloaded manually.

1. Open the Spotify podcast episode in your browser.
2. Open Developer Tools (`F12`).
3. Go to the **Network** tab.
4. Start playing the episode.
5. Search for requests containing `.mp3` or `media.mp3`.
6. Open the MP3 URL in a new tab.
7. Download the file and save it in the project directory.

Example:

```text
project/
├── transcribe.py
├── episode.mp3
└── ...
```

## Usage

Open `transcribe.py` and set the audio file name:

```python
audio_file = "episode.mp3"
```

Make sure the file is located in the same directory as the script.

Run the transcription:

```bash
python transcribe.py
```

## Output

The script generates:

```text
transcript.txt
```

containing the full transcription of the podcast episode.

Example:

```text
[0.0 - 4.2] Welcome to the podcast.

[4.2 - 7.5] Bonjour et bienvenue.

[7.5 - 11.0] Today we're going to learn French greetings.
```

## Notes

* Language detection is automatic.
* Mixed-language podcasts (e.g. English/French) are supported.
* The first run may take longer because the Whisper model needs to be downloaded.
* Larger models provide better accuracy but require more computational resources.
