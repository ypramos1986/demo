###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Input variables available: data_input (Pandas DataFrame), args (Dictionary),
# Output variables expected: best_estimator (Model), data_output (Pandas DataFrame),
#                            args (Dictionary)(**Optional)
###################################################################################

# Import modules
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Get parameters configured by user. Parameters_ui contains
# the parameters configured by the user from the UI, including 
# the ones define on the advance parameter section
n_components = args.get('parameters_ui').get('n_components')
covariance_type = args.get('parameters_ui').get('covariance_type')
tol = args.get('parameters_ui').get('tol')
max_iter = args.get('parameters_ui').get('max_iter')

# Get input data
x = data_input[args.get('selected_feature') + args.get('extra_features')]

# Train Model
x_train, x_test = train_test_split(x, test_size=0.4)
best_estimator = GaussianMixture(n_components=n_components, covariance_type=covariance_type, tol=tol, max_iter=max_iter)
best_estimator.fit(x_train)

# Get Class Prediction
prediction = best_estimator.predict(x)

# Get Class Probability Prediction
prediction_proba = best_estimator.predict_proba(x)

# Convert numpy array to pandas dataframe
prediction_pdf = pd.DataFrame(data=prediction, columns=['Prediction'])
prediction_proba_pdf = pd.DataFrame(data=prediction_proba, columns=['Prediction_Probability'])

# Create data output pandas dataframe
data_output = pd.concat([data_input[args.get('timestamp_fieldname')], prediction_pdf, prediction_proba_pdf], axis=1)

# Create performance dictionary
if len(np.unique(prediction)) >= 2:
    best_score = metrics.silhouette_score(x, prediction)
else:
    best_score = 0
performance = {"best_score": best_score}

# Create ml-properties-panel dictionary
ml_properties_panel = {"Performance": performance, 
                       "Estimator": {"n_components": n_components, "covariance_type": covariance_type, "tol": tol, "max_iter": max_iter},
                       "My parameter": {"parameter1": "Dummy parameter"}}

# Update args dictionary with metadata
args.update({"performance": performance})
args.update({"ml-properties-panel": ml_properties_panel})