###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Load model from hard drive. 
# Input variables available: args (Dictionary)
# Output variables expected: best_estimator (Model)
# Model must be loaded from the directory: args.get('local_model_path')
#########################################################################

import joblib

# Load Model
best_estimator = joblib.load(args.get('local_model_path') + '/estimator/estimator.pkl')