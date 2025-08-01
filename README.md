
#  MediBox_offline

**MediBox_offline** is a multilingual offline medical assistant that provides quick and reliable medical diagnosis based on symptoms — all without needing an internet connection.

##  Features

-  Supports four languages: English, French, Kiswahili, and Kinyarwanda
-  Symptom input via checkboxes or typing
-  Instant disease diagnosis with medical advice
-  Profile-based diagnosis history tracking
-  Offline text-to-speech for accessibility
- 100% offline — works in low-resource environments

##  Built With

- **Python** — for all core logic
- **Tkinter** — GUI framework
- **ttk** — for themed widgets
- **sqlite3** — for storing user-specific diagnosis records locally
- **pyttsx3** — offline text-to-speech engine
- **base64 & tempfile** — for icon embedding
- **datetime** — for timestamps
- **Multilingual Data** — for disease and symptom translations in 4 languages

## Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the app:**
    ```bash
    python MediBox.py
    ```

> Requires Python 3.x installed on your system.

##  File Structure

```
MediBox_offline/
├── MediBox.py
├── requirements.txt
└── README.md
```


Made with love to make healthcare more accessible — even offline.
