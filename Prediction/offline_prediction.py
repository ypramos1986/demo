###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Input variables available: best_estimator (Model), data_input (Pandas DataFrame), args (Dictionary), args_training (Dictionary)
# Output variables expected: data_output (Pandas DataFrame), args (Dictionary)(**Optional), args_training (Dictionary), (**Optional)                     
###################################################################################
# Get input
x = data_input[args.get('selected_feature') + args.get('extra_features')]

# Get Class Prediction
prediction = best_estimator.predict(x)

# Get Class Probability Prediction
prediction_proba = best_estimator.predict_proba(x)

# Convert numpy array to pandas dataframe
prediction_pdf = pd.DataFrame(data=prediction, columns=['Prediction'])
prediction_proba_pdf = pd.DataFrame(data=prediction_proba, columns=['Prediction_Probability'])

# Create data output pandas dataframe
data_output = pd.concat([data_input[args.get('timestamp_fieldname')], prediction_pdf, prediction_proba_pdf], axis=1)

# Create ml-properties-panel dictionary
ml_properties_panel = {"My parameter": {"parameter1": "Dummy parameter"}}

# Update args dictionary with metadata
args.update({"ml-properties-panel": ml_properties_panel})