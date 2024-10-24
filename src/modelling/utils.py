# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).

import os
import pickle

def pickle_object(obj, filename, folder_path='../web_service/local_objects'):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full path to save the file
    file_path = os.path.join(folder_path, f"{filename}.pkl")

    # Save the object to the file
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

    print(f"Object saved to {file_path}")

# Example usage
# Assuming 'model' is your trained linear regression model
# pickle_object(model, 'trained_linear_regression_model')
