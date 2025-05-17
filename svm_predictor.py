
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC  # SVM for classification

# Load your dataset
file_path_all_data = r"all_data.csv"
df = pd.read_csv(file_path_all_data)

# Map the DNA_loop values to labels for visualization
df['DNA_loop_label'] = df['DNA_loop'].map({0: 'Non-looping', 1: 'Looping'})

def SVM_analysis(data):
    X = data[['gc_content', 'length']]
    y = data['DNA_loop']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test)

    print("\nSupport Vector Machine (SVM) Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    # Visualize decision boundary
    w1, w2 = svm_model.coef_[0]
    b = svm_model.intercept_[0]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='gc_content', y='length', hue='DNA_loop_label', data=data,
                    palette={'Non-looping': 'red', 'Looping': 'blue'})
    x_vals = np.linspace(data['gc_content'].min(), data['gc_content'].max(), 100)
    y_vals = -(w1 / w2) * x_vals - b / w2
    plt.plot(x_vals, y_vals, color='black', linestyle='--', label='SVM Decision Boundary')
    plt.title('SVM Decision Boundary for DNA Loop Prediction')
    plt.xlabel('GC Content')
    plt.ylabel('Length')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"SVM Decision Boundary Equation: Length = {-(w1 / w2):.2f} * GC Content + {-(b / w2):.2f}")

if __name__ == "__main__":
    SVM_analysis(df)
