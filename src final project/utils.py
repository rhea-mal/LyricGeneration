import librosa
import numpy as np

def z_score_normalize(value, mean, std):
    return (value - mean) / std

def get_duration(path):
    mean_duration = 221067.3859
    std_duration = 74448.6686
    duration_sec = librosa.get_duration(path=path)
    return z_score_normalize(duration_sec * 1000, mean_duration, std_duration) 

def get_danceability(y, sr):
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo_normalized = tempo / 250.0  
    
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    beat_intervals = np.diff(beat_times)
    beat_interval_std = np.std(beat_intervals)
    
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    pulse = librosa.beat.plp(onset_envelope=onset_env, sr=sr)
    rhythm_stability = np.std(pulse) 
    beat_strength = np.mean(librosa.util.normalize(onset_env))
    
    S = np.abs(librosa.stft(y))
    contrast = np.mean(librosa.feature.spectral_contrast(S=S, sr=sr))
    regularity = 1.0 - (contrast / 100.0)  
    
    danceability = (tempo_normalized * 0.4 + beat_strength * 0.3 + regularity * 0.3)
    danceability = np.clip(danceability, 0.0, 1.0)
    
    mean_danceability = 1.7591
    std_danceability = 0.4957
    scaled_danceability = (danceability - mean_danceability) / std_danceability
    
    return scaled_danceability
    

def get_energy(y, sr):
    rms = librosa.feature.rms(y=y)[0]
    energy = np.mean(rms)

    mean_energy = 0.6302
    std_energy = 0.2522
    scaled_energy = (energy - mean_energy) / std_energy
    
    return scaled_energy

def get_popularity():
    return 5
def get_key(y, sr):
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)


    mean_chroma = np.mean(chromagram, axis=1)
    
    chroma_to_key = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key_to_index = { 
    'G': 0,
    'G#': 1,
    'A': 2,
    'A#': 3,
    'B': 4,
    'C': 5,
    'C#': 6,
    'D': 7,
    'D#': 8,
    'E': 9,
    'F': 10,
    'F#': 11
}
    
    estimated_key_index = np.argmax(mean_chroma)
    estimated_key = chroma_to_key[estimated_key_index]

    return key_to_index[estimated_key]

def get_loudness(y, sr):
    mean_loudness = -15.7429
    std_loudness = 8.9676
    
    S = np.abs(librosa.stft(y))
    rms = librosa.feature.rms(S=S)
    loudness = np.mean(rms)
    scaled_loudness = (loudness - mean_loudness) / std_loudness
    
    return scaled_loudness

def get_acousticness(y, sr):
    mean_acousticness = 0.2912
    std_acousticness = 0.3314
    
    S = np.abs(librosa.stft(y))
    centroid = librosa.feature.spectral_centroid(S=S)
    acousticness = np.mean(1 - (centroid / np.max(centroid)))
    return z_score_normalize(acousticness, mean_acousticness, std_acousticness)

def get_instrumentalness(y, sr):
    mean_instrumentalness = 0.1510
    std_instrumentalness = 0.2985
    
    S = np.abs(librosa.stft(y))
    contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
    vocal_band_contrast = np.mean(contrast[2])  
    instrumentalness = 1 - vocal_band_contrast / np.max(contrast)
    return z_score_normalize(instrumentalness, mean_instrumentalness, std_instrumentalness)


def get_liveness(y, sr):
    mean_liveness = 0.0880
    std_liveness = 0.0659
    
    o_env = librosa.onset.onset_strength(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    liveness = np.mean(rms) / np.max(o_env)  
    return z_score_normalize(liveness, mean_liveness, std_liveness)

def get_valence(y, sr):
    mean_valence = 0.4411
    std_valence = 0.2367
    
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    major = np.mean(chroma[4]) + np.mean(chroma[7]) 
    minor = np.mean(chroma[3]) + np.mean(chroma[7]) 
    valence = major / (major + minor)
    return z_score_normalize(valence, mean_valence, std_valence)

def get_tempo(y, sr):
    mean_tempo = 246.1688
    std_tempo = 59.3314
    
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    return z_score_normalize(tempo, mean_tempo, std_tempo)

def create_prompts(y, sr, artist, genre, explicit, duration):
    '''
    FEATURE WEIGHTS:
    'tempo': 4.5, '
    'valence': 4.0, 
    'popularity': 4.0,
    'danceability': 3.5,
    'energy': 4.5,
    'loudness': 3.0,
    'speechiness': 2.5,
    'acousticness': 3.5,
    'instrumentalness': 3.5,
    'liveness': 3.0,
    'explicit': 2.5
    
    '''
    duration_in_samples = len(y)
    prompts = []
    num_segments = 4
    segment_length = duration_in_samples // num_segments  
    for i in range(num_segments):
        start_sample = i * segment_length
        end_sample = start_sample + segment_length
        cropped_song = y[start_sample:end_sample]
        
        
        prompt = ('<DURATION_MS: ' + str(duration) + '> ' + 
                  '<POPULARITY: ' + str(get_popularity()) + '> ' + 
                '<DANCEABILITY: ' + str(get_danceability(cropped_song, sr) * 3.5) + '> ' +
                '<ENERGY: ' + str(get_energy(cropped_song, sr) * 4.5) + '> ' +
                '<LOUDNESS: ' + str(get_loudness(cropped_song, sr) * 3.0) + '> ' + 
                '<ACOUSTICNESS: ' + str(get_acousticness(cropped_song, sr)* 3.5)  + '> ' +
                '<INSTRUMENTALNESS: ' + str(get_instrumentalness(cropped_song, sr) * 3.5) + '> ' + 
                '<LIVENESS: ' + str(get_liveness(cropped_song, sr) * 3.0) + '> ' + 
                '<VALENCE: ' + str(get_valence(cropped_song, sr) * 4.0) + '> ' + 
                '<TEMPO: ' + str(get_tempo(cropped_song, sr) * 4.5) + '> ' + 
                '<EXPLICIT: ' + str(explicit * 2.5) + '> ' +
                '<ARTIST: ' + artist.lower() + '> ' +
                '<TRACK_GENRE: ' + genre.lower() + '>')
        prompts.append(prompt)
    return prompts