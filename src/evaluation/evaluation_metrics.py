from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)
import matplotlib.pyplot as plt
import seaborn as sns


def print_evaluation_metrics(y_true, y_pred, y_pred_proba) -> None:
    print("-----" * 15)
    print("Confusion Matrix: \n", confusion_matrix(y_true, y_pred))

    print("-----" * 15)
    print("Accuracy : \n", accuracy_score(y_true, y_pred) * 100)

    print("-----" * 15)
    print("Report : \n", classification_report(y_true, y_pred))

    print("-----" * 15)
    print("ROC-AUC: \n", roc_auc_score(y_true, y_pred_proba[:, 1]))


def plot_roc_curve(y_true, y_pred_proba):
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba[:, 1])
    plt.plot(fpr, tpr, label="ROC curve")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random classifier")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curve")
    plt.legend()
    plt.show()


def plot_heatmap_confusion_matrix(y_true, y_pred):
    sns.heatmap(confusion_matrix(y_true, y_pred), annot=True, cmap="YlGnBu", fmt="d")
