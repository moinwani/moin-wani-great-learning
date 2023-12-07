import pandas as pd

# Load the CSV file
data = pd.read_csv("iris.csv")

# Separate features and target
features = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
target = data["species"] # or "class"

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Train the model
model = LogisticRegression(solver="lbfgs")
model.fit(X_train, y_train)

from joblib import dump, load

# Save the model
dump(model, "model.joblib")

# Load the model
model = load("model.joblib")



