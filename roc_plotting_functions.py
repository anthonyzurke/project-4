import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from IPython.display import display_html




def plot_model(threshold, y_test, probas1, descrip1, probas2=[], descrip2 = False):
    """
    Functions takes a threshold value, predicted probabilities of income >50K and a description of the model.

    Additional model probabilities can be displayed side by side if entered.
    """
    ### helper function

    def display_side_by_side(*args):
        html_str=''
        for df in args:
            html_str+=df.to_html()
        display_html(html_str.replace('table','table style="display:inline"'),raw=True)
        
    def get_predictions(probabilities, threshold):
        return ['<=50K' if prob < threshold else '>50K' for prob in probabilities]

    ### helper function
    def get_plotting_info(probas, thresh):
        predictions = get_predictions(probas, thresh)

        fprs, tprs, _ = roc_curve(y_test, probas, pos_label='>50K')
        fpr_model = confusion_matrix(y_test, predictions)[0][1]/ sum(confusion_matrix(y_test, predictions)[0])
        tpr_model = confusion_matrix(y_test, predictions)[1][1]/ sum(confusion_matrix(y_test, predictions)[1])

        acc_score = accuracy_score(y_test, predictions)

        return fprs, tprs, fpr_model, tpr_model, acc_score, predictions

    ### main function
    fprs, tprs, fpr_model, tpr_model, accuracy, predictions = get_plotting_info(probas1, threshold)
    dct = {}
    dct[descrip1] = [round(accuracy,4), round(roc_auc_score(y_test, probas1), 4)]

    if len(probas2) > 0:
        fprs2, tprs2, fpr_model2, tpr_model2, accuracy2, predictions2 = get_plotting_info(probas2, threshold)
        dct[descrip2] = [round(accuracy2,4), round(roc_auc_score(y_test, probas2), 4)]

    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(fprs, tprs, label=descrip1, color='blue')
    if len(probas2) > 0:
        ax.plot(fprs2, tprs2, label=descrip2, color='orange')
    ax.plot([0,1], [0,1], linestyle='--', color='black')
    ax.plot(fpr_model, tpr_model, marker = 'o', linewidth=20, color = 'blue')
    if len(probas2) > 0:
        ax.plot(fpr_model2, tpr_model2, marker = 'o', linewidth=20, color = 'orange')
    ax.set_ylabel('True Positive Rate', fontsize=18)
    ax.set_xlabel('False Positive Rate', fontsize=18)
    ax.legend()
    display(pd.DataFrame(dct, index=['Accuracy Score', 'AUC_ROC']))
    cm1 = pd.DataFrame(confusion_matrix(y_test, predictions),columns=pd.MultiIndex.from_product([[descrip1], ['Predicted <=50K', 'Predicted >50K']]),\
             index=['True <=50K', 'True >50K'])
    if len(probas2) > 0:
        cm2 = pd.DataFrame(confusion_matrix(y_test, predictions2),columns=pd.MultiIndex.from_product([[descrip2], ['Predicted <=50K', 'Predicted >50K']]),\
             index=['True <=50K', 'True >50K'])
        display_side_by_side(cm1, cm2)
    else:
        display(cm1)
