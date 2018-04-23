import numpy as np
import matplotlib.pyplot as plt


def plot_feature_importance(feature_importances, title, feature_names):
    feature_importances = 100.0 * (feature_importances / max(feature_importances))
    index_sort = np.flipud(np.argsort(feature_importances))
    pos = np.arange(index_sort.shape[0]) + 0.5
    plt.figure()
    plt.bar(pos, feature_importances[index_sort], align='center')
    print feature_names
    plt.xticks(pos, feature_names[index_sort])
    plt.ylabel('Relative Importance')
    plt.title(title)
    plt.show()

def plot_classifier(classifier,X,y):
	x_min,x_max = X[:,0].min()-1, X[:,0].max()+1
	y_min,y_max = X[:,1].min()-1, X[:,1].max()+1

	step_size = 1
	x_values, y_values = np.meshgrid(np.arange(x_min,x_max,step_size),np.arange(y_min,y_max,step_size))

	