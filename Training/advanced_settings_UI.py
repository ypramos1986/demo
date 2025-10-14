###################################################################################
# THIS CODE IS A DUMMY/GENERIC EXAMPLE
###################################################################################
# Advanced settings dictionary can be accessed using: args.get('parameters_ui')
# To Access specific parameter: args.get('parameters_ui').get('parameter_name')  
################################################################################
advanced_settings_form = {
  "training_parameters": {
    "ui-config": {
      "name": "Training Parameters",
      "description": "Training Parameters to be set by user",
      "config": {
        "hyperparameters": {
          "name": "Enable hyperparameters",
          "type": "boolean",
          "default": True
        },
        "covariance_type": {
          "name": "Covariance Type",
          "description": "String describing the type of covariance parameters to use",
          "type": "selector",
          "default": "full",
          "required": True,
          "options": [
            {"label": "full", "value": "full"},
            {"label": "tied", "value": "tied"},
            {"label": "diag", "value": "diag"},
            {"label": "spherical", "value": "spherical"}
          ],
          "jsExpressionProperties": {
            "disabled": "!section.hyperparameters"
          }
        },
        "tol": {
          "name": "Tolerance",
          "description": "The convergence threshold. EM iterations will stop when the lower bound average gain is below this threshold.",
          "required": True,
          "type": "number",
          "default": 0.001,
          "min": 0,
          "max": 1,
          "step": 0.001
        },
        "n_components": {
          "name": "Number of Components",
          "description": "The number of mixture components",
          "required": True,
          "type": "number",
          "default": 1,
          "min": 1,
          "step": 1
        },
        "max_iter": {
          "name": "Max Iteration",
          "description": "Maximum number of iterations",
          "required": True,
          "type": "number",
          "default": 100,
          "min": 1,
          "step": 1
        }
      }
    }
  }
}