# 🎤 AI Udio Forensics Tool 🕵️‍♂️

**Udio Forensics Tool** is a desktop application designed for forensic analysis of audio files. This tool allows you to detect manipulations, anomalies, and technical characteristics of audio recordings, providing a detailed report in PDF format. Ideal for investigators, forensic experts, and anyone who needs to analyze audio files professionally. 🔍🎧

---

## 🚀 Key Features

- **🎚️ Technical Audio Analysis**:
  - Extract information such as sample rate, bit depth, duration, format, and file size.

- **📊 Spectral Analysis**:
  - Generate a spectrogram to visualize the frequency components of the audio signal.

- **🔍 Anomaly Detection**:
  - Calculate zero-crossing rate, average and maximum loudness, silent segments, and the duration of the longest non-silent segment.

- **⚠️ Tampering Detection**:
  - Identify cuts, splices, or other discontinuities in the audio signal.

- **🗣️ Speech-to-Text Transcription**:
  - Automatically transcribe spoken content into text using Deepseek's API.

- **😊 Emotion Recognition**:
  - Analyze the tone of voice to detect emotions such as anger, fear, happiness, or sadness.

- **👤 Speaker Identification**:
  - Identify and separate the voices of different speakers in an audio file.

- **🔊 Noise Reduction**:
  - Remove background noise to improve audio quality and facilitate analysis.

- **📈 Advanced Tampering Detection**:
  - Detect sophisticated manipulations like audio overlays, tone modifications, or segment removals.

- **👤 Voice Recognition**:
  - Identify the speaker by comparing the voice with a database of known voices.

- **🎵 Pitch and Frequency Analysis**:
  - Analyze the pitch and frequency of the voice to detect anomalies or manipulations.

- **📄 PDF Report Generation**:
  - Create a detailed PDF report with analysis results, including graphs and technical data.

---

## 🛠️ Technologies Used

- **🐍 Python**: Main programming language.
- **📦 Python Libraries**:
  - `PyQt5`: For the graphical user interface.
  - `soundfile` and `librosa`: For audio processing and analysis.
  - `matplotlib`: For generating graphs.
  - `reportlab`: For creating PDF reports.
  - `requests`: For making HTTP requests to Deepseek's API.
- **🖼️ Graphical User Interface**: Simple and intuitive, designed for immediate use.

---

## 🔑 API Key Configuration

To use features that rely on external APIs (e.g., Deepseek), you need to provide your API keys. Here’s how to configure them:

### **1. Deepseek API Key**
   - **File**: `audio_handler.py`
   - **Steps**:
     1. Obtain your API key from [Deepseek](https://www.deepseek.com).
     2. Replace `"DEEPSEEK API KEY"` in the `audio_handler.py` file with your actual API key.
     ```python
     headers = {
         'Authorization': 'Bearer DEEPSEEK API KEY'  # Replace with your actual API key
     }
     ```

### **2. Environment Variables (Optional)**
   - For better security, you can store your API keys in environment variables.
   - **Steps**:
     1. Create a `.env` file in the project root:
        ```plaintext
        DEEPSEEK_API_KEY=your_api_key_here
        ```
     2. Update the code to load the API key from the environment:
        ```python
        import os
        api_key = os.getenv('DEEPSEEK_API_KEY')
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        ```

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tuo-repository/UdioForensicsTool.git
   cd UdioForensicsTool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**:
   - Follow the instructions in the **API Key Configuration** section above.

4. **Run the application**:
   ```bash
   python main.py
   ```

---

## 🖥️ How to Use the Application

1. **Load an audio file**:
   - Click on "Load Audio File" and select a supported audio file (e.g., `.wav`, `.mp3`, `.flac`).

2. **Start the analysis**:
   - Click on "Analyze and Detect Manipulations" to start the complete analysis.

3. **View the results**:
   - The analysis results will be displayed in the graphical interface and saved in a PDF report.

4. **Export the report**:
   - The PDF report will be saved in the same folder as the analyzed audio file.

---

## 📂 Project Structure

```
UdioForensicsTool/
├── audio_handler.py          # Handles audio file information and advanced features
├── anomaly_detection.py      # Detects anomalies in the audio signal
├── spectral_analysis.py      # Generates the spectrogram
├── tampering_detection.py    # Detects tampering in the audio file
├── report_generator.py       # Generates the PDF report
├── gui.py                    # Graphical user interface of the application
├── main.py                   # Entry point of the application
├── requirements.txt          # Project dependencies
├── .env                      # Optional: Store API keys securely
└── README.md                 # Project documentation
```

---

## 📄 Example of PDF Report

The generated report includes:
- **Introduction**: General information about the audio file.
- **Technical Characteristics**: Details such as duration, format, channels, sample rate, and resolution.
- **Audio Content Analysis**: Average and maximum loudness, silent segments, and duration of the longest non-silent segment.
- **Spectrogram**: Visualization of the frequency components of the audio signal.
- **Discontinuity Analysis**: Graph of detected discontinuities.
- **Speech Transcription**: Transcribed text of the spoken content.
- **Emotion Detection**: Detected emotions in the audio.
- **Speaker Identification**: Results of speaker identification.
- **Noise Reduction**: Path to the cleaned audio file.
- **Advanced Tampering Detection**: Results of advanced tampering analysis.
- **Voice Recognition**: Results of voice recognition.
- **Pitch and Frequency Analysis**: Analysis of pitch and frequency.

---

## 🤝 Contributions

If you wish to contribute to the project, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

---

## 📜 License

This project is released under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

---

## 👨‍💻 Author

**M. C.**  


---

Thank you for choosing **Udio Forensics Tool**! 🎉  
If you have any questions or suggestions, feel free to contact me. 😊

---

Fammi sapere se hai bisogno di ulteriori modifiche o chiarimenti! 😊
