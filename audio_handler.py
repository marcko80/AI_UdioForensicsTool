import soundfile as sf
import os
import requests
import numpy as np
import librosa
import noisereduce as nr

def get_audio_info(audio_file):
    """
    Estrae le informazioni tecniche del file audio per Udio Forensics Tool.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        info = sf.info(audio_file)
        # Calcola la profondità di bit in base al tipo di dato
        bit_depth = data.dtype.itemsize * 8 if hasattr(data, 'dtype') else 'N/A'
        
        # Estrai il formato del file dall'estensione
        file_format = os.path.splitext(audio_file)[1].replace('.', '').upper()

        return {
            'filename': os.path.basename(audio_file),
            'sample_rate': info.samplerate,
            'bit_depth': bit_depth,
            'channels': info.channels,
            'duration': info.duration,
            'file_size': os.path.getsize(audio_file),
            'format': file_format  # Aggiunto il formato del file
        }
    except Exception as e:
        print(f"Errore durante l'estrazione delle informazioni: {e}")
        return None

def transcribe_audio(audio_file):
    """
    Trascrive il contenuto parlato di un file audio utilizzando l'API di Deepseek.
    """
    try:
        # URL dell'API di Deepseek per la trascrizione
        url = "https://api.deepseek.com/v1/transcribe"
        
        # Leggi il file audio
        with open(audio_file, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': 'Bearer DEEPSEEK API KEY'  # Sostituisci con la tua chiave API
            }
            response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('transcription', 'N/A')
        else:
            print(f"Errore durante la trascrizione: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Errore durante la trascrizione: {e}")
        return None

def detect_emotions(audio_file):
    """
    Rileva le emozioni nel parlato utilizzando l'API di Deepseek.
    """
    try:
        # URL dell'API di Deepseek per il rilevamento delle emozioni
        url = "https://api.deepseek.com/v1/emotion"
        
        # Leggi il file audio
        with open(audio_file, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': 'Bearer DEEPSEEK API KEY'  # Sostituisci con la tua chiave API
            }
            response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('emotions', 'N/A')
        else:
            print(f"Errore durante il rilevamento delle emozioni: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Errore durante il rilevamento delle emozioni: {e}")
        return None

def identify_speaker(audio_file, reference_audio):
    """
    Identifica il parlante confrontando la voce con un file audio di riferimento.
    """
    try:
        # URL dell'API di Deepseek per l'identificazione del parlante
        url = "https://api.deepseek.com/v1/speaker-identification"
        
        # Leggi i file audio
        with open(audio_file, 'rb') as file1, open(reference_audio, 'rb') as file2:
            files = {'file1': file1, 'file2': file2}
            headers = {
                'Authorization': 'Bearer DEEPSEEK API KEY'  # Sostituisci con la tua chiave API
            }
            response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('match', 'N/A')
        else:
            print(f"Errore durante l'identificazione del parlante: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Errore durante l'identificazione del parlante: {e}")
        return None

def reduce_noise(audio_file, output_file):
    """
    Riduce il rumore di fondo da un file audio utilizzando noisereduce.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        reduced_noise = nr.reduce_noise(y=data, sr=sample_rate)
        sf.write(output_file, reduced_noise, sample_rate)
        return output_file
    except Exception as e:
        print(f"Errore durante la riduzione del rumore: {e}")
        return None

def detect_advanced_tampering(audio_file):
    """
    Rileva manipolazioni avanzate nel file audio utilizzando l'API di Deepseek.
    """
    try:
        # URL dell'API di Deepseek per il rilevamento di manipolazioni avanzate
        url = "https://api.deepseek.com/v1/advanced-tampering"
        
        # Leggi il file audio
        with open(audio_file, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': 'Bearer DEEPSEEK API KEY'  # Sostituisci con la tua chiave API
            }
            response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('tampering_results', 'N/A')
        else:
            print(f"Errore durante il rilevamento delle manipolazioni avanzate: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Errore durante il rilevamento delle manipolazioni avanzate: {e}")
        return None

def recognize_voice(audio_file, voice_database):
    """
    Riconosce la voce confrontandola con un database di voci note.
    """
    try:
        # URL dell'API di Deepseek per il riconoscimento vocale
        url = "https://api.deepseek.com/v1/voice-recognition"
        
        # Leggi il file audio e il database di voci
        with open(audio_file, 'rb') as file:
            files = {'file': file, 'database': voice_database}
            headers = {
                'Authorization': 'Bearer DEEPSEEK API KEY'  # Sostituisci con la tua chiave API
            }
            response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('voice_match', 'N/A')
        else:
            print(f"Errore durante il riconoscimento vocale: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Errore durante il riconoscimento vocale: {e}")
        return None

def analyze_pitch_and_frequency(audio_file):
    """
    Analizza il tono e la frequenza della voce.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        pitch, _ = librosa.piptrack(y=data, sr=sample_rate)
        mean_pitch = np.mean(pitch)
        return {
            'mean_pitch': mean_pitch,
            'sample_rate': sample_rate
        }
    except Exception as e:
        print(f"Errore durante l'analisi del tono e della frequenza: {e}")
        return None