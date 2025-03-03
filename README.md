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
MFCCs are widely used features in speech and speaker recognition because they effectively capture the unique characteristics of a speaker's voice.
- They capture vocal tract characteristics, making them useful for distinguishing different speakers.
- They reduce noise sensitivity compared to raw audio waveforms.
- They provide a compact representation of speech signals, making them efficient for machine learning models.

In a typical set of MFCC coefficients, each coefficient captures different aspects of the audio signal. Here are brief explanations for a few of them:

- First Coefficient (MFCC 0): Often referred to as the "constant" term, it represents the overall energy of the signal.

- Second Coefficient (MFCC 1): Represents the overall spectral slope and is related to the perceived pitch.

- Third Coefficient (MFCC 2): Captures spectral features related to the shape of the vocal tract and is associated with formants in speech.

- Fourth Coefficient (MFCC 3): Reflects changes in the spectral envelope and can be related to nasality in speech.

- Higher-order Coefficients (MFCC 4 and above): Capture more detailed spectral characteristics, providing information about fine spectral structures in the audio.

### Model Setup and Training
This model is a Recurrent Neural Network (RNN) using an LSTM (Long Short-Term Memory) layer to process sequential audio features for speaker recognition.

+ The first layer is an LSTM layer with 128 units, which captures temporal dependencies from the MFCC feature sequences.
+ The second layer is a fully connected Dense layer with 64 neurons and ReLU activation, adding a non-linearity to help the model learn complex patterns.
+ The final output layer has neurons equal to the number of speakers, with a softmax activation function to output probability distributions over the speaker classes.
### Why Use RNN?
RNNs, particularly LSTMs (Long Short-Term Memory networks), are well-suited for sequence-based data like audio signals.
- Sequential Data Handling – Audio features (like MFCCs) are time-dependent, meaning past frames influence the present. LSTMs are designed to handle this temporal relationship effectively.

- Memory of Past Information – Unlike traditional feedforward networks, LSTMs have gates that allow them to retain or forget information, making them ideal for capturing long-term dependencies in speech.

- Better Context Understanding – Speaker-specific features may appear at different points in time, and LSTMs help in preserving context over a sequence, leading to more accurate speaker identification.

### Why Not CNNs or Other Models?
+ CNNs work well for spatial data like images but don’t naturally handle sequential dependencies in audio unless used with 1D convolutions or transformers.
+ Transformers (e.g., Attention-based models) are powerful but require much more data and computational resources than LSTMs for speech tasks.
+ Traditional MLPs (Dense Networks) ignore temporal relationships, making them less effective for speaker recognition.
  
Thus, LSTMs strike a balance between efficiency and performance, making them a great choice for small-scale speaker recognition projects. 
