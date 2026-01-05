# 📈 BioScope: Multi-Channel Biological Signal Viewer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![GUI](https://img.shields.io/badge/GUI-PyQt5-green)
![Library](https://img.shields.io/badge/Graphing-PyQtGraph-orange)
![Domain](https://img.shields.io/badge/Domain-Biomedical%20Signals-red)

## 📌 Project Overview
**BioScope** is a desktop application designed for visualizing and analyzing multi-channel biological signals (such as ECG, EMG, and EEG). It provides a robust interface for researchers and medical professionals to load, view, and manipulate signal data from various file formats.

The application supports real-time simulation (cine-mode), signal manipulation (zoom, pan, scroll), and handling of multiple channels simultaneously with high performance.

## ⚙️ Key Features
* **Multi-Format Support:** Load signals from `.csv`, `.txt`, and `.mat` (Matlab) files.
* **Multi-Channel Visualization:** Plot multiple signals in separate, synchronized viewports.
* **Playback Controls:**
    * **Cine Mode:** Auto-scrolling simulation of real-time signal acquisition.
    * **Controls:** Play, Pause, Stop, Rewind, and Speed control.
* **Interactive Graphing:**
    * Zoom in/out and Pan (Scroll) through long recordings.
    * Change signal colors and visibility.
    * Show/Hide legends and grid lines.
* **Signal Analysis:** Display signal statistics (Min, Max, Mean, Duration).

## 🛠️ Tech Stack
* **Language:** Python.
* **GUI Framework:** PyQt5 (Qt Designer).
* **Plotting Library:** PyQtGraph (for high-performance real-time plotting) or Matplotlib.
* **Data Handling:** Pandas, NumPy, SciPy (for .mat files).

## 🚀 How to Run
1.  **Clone the repository**
2.  **Install Dependencies**
3.  **Run the Application:**
    ```bash
    python src/main.py
    ```

## 📂 Supported Signals
The `data` directory contains sample datasets for testing:
* **ECG:** Cardiac electrical activity.
* **EMG:** Muscle electrical activity.
* **EEG:** Brain electrical activity.