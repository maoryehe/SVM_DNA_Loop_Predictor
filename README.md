
# DNA Loop Prediction using SVM

This project analyzes DNA sequences to predict whether they form chromatin loops mediated by cMyc/MAX transcription factors. It leverages sequence features like GC content and length to train a Support Vector Machine (SVM) classifier.

## Features
- Reads sequence data (GC content + length)
- Trains a linear SVM to classify loop vs. non-loop sequences
- Includes a user-friendly GUI (Tkinter) to predict loop formation from raw DNA sequence input
- Displays sequence length, GC content, and prediction outcome

## Folder Structure
```
SVM_DNA_Loop_Predictor/
├── data/
│   └── all_data_below_0.8.csv      # CSV file with 'gc_content', 'length', 'DNA_loop'
├── svm_predictor.py                # Console-based model training and decision boundary visualization
├── dna_loop_gui.py                 # GUI to enter DNA sequences and get predictions
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the GUI
```bash
python dna_loop_gui.py
```

### 3. Enter a DNA sequence
You’ll get:
- Length of sequence
- GC content
- Prediction: ✅ loop / ❌ no loop

## Data Format
The dataset should include the following columns:
- `gc_content` – float between 0 and 1
- `length` – integer length of the DNA segment
- `DNA_loop` – binary (1 = looping, 0 = non-looping)

## Credits
Developed by Maor Yehezkehely  
Research inspired by structural analysis of cMyc/MAX-DNA interactions and chromatin looping in embryonic stem cells.

---

