# SIC-AI-Project

This project was completed as my Capstone Project at Samsung Innovation Campus.

## Speaker Recognition Using Deep Learning.
This project focuses on speaker recognition, where a neural network is trained to identify individuals based on their voice. It involves audio preprocessing, feature extraction (MFCCs), and model training using deep learning techniques.
The dataset consists of recorded audio samples, which are processed and transformed into Mel-Frequency Cepstral Coefficients (MFCCs) for training a neural network.

### Audio Preprocessing
The preprocessing phase involves resampling the audio to a consistent sample rate, trimming and splitting long recordings into 1-second segments, extracting MFCC features for numerical representation, normalizing the features and encoding speaker labels

**Dependencies**:  
Install required libraries if not installed:
+ pip install librosa soundfile
  
Refer to this Python code for preprocessing: [preprocessing.py](./preprocessing.py)  
### Feature Extraction
In the feature extraction phase, Mel-Frequency Cepstral Coefficients (MFCCs) are computed from the audio signals. MFCCs capture the spectral characteristics of speech, making them effective for speaker recognition. 
