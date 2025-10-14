###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Input variables available: best_estimator (Model), data_input (Pandas DataFrame), args (Dictionary), best_estimator_parameters (Dictionary)
# Output variables expected: data_output (Pandas DataFrame)                    
###################################################################################
# Access the model instance settings if it is needed
model_instance_settings = args.get('model_instance_settings')

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