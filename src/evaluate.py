from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(y_true, y_pred):
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))
