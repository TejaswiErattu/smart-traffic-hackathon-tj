# train_model.py

import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # ✅ Correct import
import joblib

# Generate synthetic data
data = []
for _ in range(500):
    vehicle_count = random.randint(0, 20)
    emergency = random.choice([0, 1])
    
    # Simulated logic to determine state
    if emergency:
        state = "GREEN"
    elif vehicle_count > 10:
        state = "GREEN"
    elif vehicle_count < 3:
        state = "RED"
    else:
        state = "YELLOW"
        
    data.append([vehicle_count, emergency, state])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["vehicle_count", "emergency", "state"])

# Encode states as numbers
df["state_encoded"] = df["state"].map({"RED": 0, "YELLOW": 1, "GREEN": 2})

# Features and target
X = df[["vehicle_count", "emergency"]]
y = df["state_encoded"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model to disk
joblib.dump(model, "ai_model.pkl")

print("✅ AI model trained and saved to ai_model.pkl")
