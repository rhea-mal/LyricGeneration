from utils import *
from lyric_generation import *
import tempfile

def start_generation(artist, genre, explicit, uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Load the audio file using librosa
    y, sr = librosa.load(tmp_file_path, sr=None)
    duration_sec = librosa.get_duration(path=tmp_file_path)
    prompts = create_prompts(y, sr, artist, genre, explicit, duration_sec)
    segments = []
    for prompt in prompts:
        segments.append(prompt)
    lyrics = process_librosa_input(segments[0])
    return lyrics