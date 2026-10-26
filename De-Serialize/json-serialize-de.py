import json

# A live Python dictionary in RAM
user_data = {"name": "Alice", "is_admin": True, "roles": [1, 2]}

# --- SERIALIZATION ---
# Convert Python object to a JSON formatted text string
json_string = json.dumps(user_data)
print(json_string)  
# Output: '{"name": "Alice", "is_admin": true, "roles": [1, 2]}' 
# (Notice True became lowercase true to match standard JSON)

# --- DESERIALIZATION ---
# Convert the JSON string back into a live Python dictionary
original_object = json.loads(json_string)
