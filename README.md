# Python Audio Analysis

A foundational music information retrieval (MIR) script to extract musical data from audio files. 

### The Project
This script bridges digital signal processing with visual data representation. For this test, I analyzed a short guitar recording to extract tempo and visualize the frequency spectrum.

### Tools Used
* **Python**
* **Librosa:** Used for beat tracking and audio feature extraction.
* **Matplotlib:** Used to generate the visualization.

### How It Works
1. Loads a `.wav` file into an array.
2. Calculates the estimated tempo (BPM) of the performance.
3. Generates a Mel-Spectrogram (frequency over time) and converts the power spectrum to decibels (dB) for accurate acoustic visualization.

*(Check out the attached `.png` file to see the spectrogram output!)*
