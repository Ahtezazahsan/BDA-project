import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pymongo import MongoClient
import librosa
import zipfile
from tqdm import tqdm

# Load metadata from the provided zip file
with zipfile.ZipFile('/home/ahtezaz/fma_metadata.zip', 'r') as zip_ref:
    zip_ref.extractall('metadata_temp')

# Read metadata files
albums_df = pd.read_csv('metadata_temp/albums.csv')
artists_df = pd.read_csv('metadata_temp/artists.csv')
genres_df = pd.read_csv('metadata_temp/genres.csv')
tracks_df = pd.read_csv('metadata_temp/tracks.csv')

# Merge metadata based on track_id
metadata_df = pd.merge(tracks_df, albums_df, on='album_id', how='left')
metadata_df = pd.merge(metadata_df, artists_df, on='artist_id', how='left')
metadata_df = pd.merge(metadata_df, genres_df, on='track_id', how='left')

# List audio files in the specified directory
audio_files = []
for root, dirs, files in os.walk('/home/ahtezaz/music/sample_size'):
    for file in files:
        if file.endswith(".mp3"):
            audio_files.append(os.path.join(root, file))

# Extract features from audio files
features = []
for audio_file in audio_files:
    try:
        y, sr = librosa.load(audio_file, sr=None)
    except Exception as e:
        print(f"Warning: Failed to load audio file '{audio_file}': {e}")
        continue
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]

    audio_features = []
    for feature in [mfcc, spectral_centroid, zero_crossing_rate]:
        audio_features.append(np.mean(feature))
        audio_features.append(np.std(feature))
        audio_features.append(np.median(feature))
    
    features.append(audio_features)

# Preprocess features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

pca = PCA(n_components=5)
reduced_features = pca.fit_transform(scaled_features)

# Upload features and metadata to MongoDB
client = MongoClient('192.168.93.129', 27017)
db = client['music_features']
collection = db['audio_features']

for i, (feature, row) in tqdm(enumerate(zip(reduced_features, metadata_df.iterrows())), total=len(reduced_features), desc="Uploading data to MongoDB"):
    track_id = row[1]['track_id']
    document = {
        "track_id": track_id,
        "features": feature.tolist(),
        "metadata": row[1].to_dict()
    }
    collection.insert_one(document)

# Remove temporary directory
os.rmdir('metadata_temp')
