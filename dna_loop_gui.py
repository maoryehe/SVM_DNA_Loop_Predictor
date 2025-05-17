
import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib

# Load dataset and train SVM
df = pd.read_csv(r"C:\Users\maory\OneDrive\Desktop\‏‏all_data_below_0.8.csv" )
X = df[['gc_content', 'length']]
y = df['DNA_loop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Save the model for future use
joblib.dump(svm_model, "svm_model.joblib")


# GUI Application
def predict_loop():
    sequence = entry.get().upper()
    if not set(sequence).issubset({'A', 'C', 'G', 'T'}):
        messagebox.showerror("Invalid Input", "Sequence must contain only A, C, G, T characters.")
        return

    length = len(sequence)
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = gc_count / length if length > 0 else 0

    # Prepare input and predict
    input_data = np.array([[gc_content, length]])
    prediction = svm_model.predict(input_data)[0]

    result = "Loop predicted ✅" if prediction == 1 else "No loop predicted ❌"
    result_text = (
        f"Sequence Length: {length}\n"
        f"GC Content: {gc_content:.2f}\n"
        f"Prediction: {result}"
    )
    output_label.config(text=result_text)


# Create GUI
root = tk.Tk()
root.title("DNA Loop Prediction")

tk.Label(root, text="Enter DNA Sequence:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

predict_button = tk.Button(root, text="Predict DNA Loop", command=predict_loop)
predict_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
output_label.pack(pady=10)

root.mainloop()
