###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Save model to hard drive. 
# Input variables available: best_estimator (Model), args (Dictionary)
# Output variables expected: None
# Model must be save to the directory: args.get('local_model_path')
#########################################################################

import joblib

# Save model
os.makedirs(args.get('local_model_path') + '/estimator', exist_ok=True)
joblib.dump(best_estimator, args.get('local_model_path') + '/estimator/estimator.pkl')