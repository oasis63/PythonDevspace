import pickle

data = {"score": 42, "items": ["sword", "shield"]}

# --- SERIALIZATION (Pickling) ---
# Convert to a binary byte stream
byte_stream = pickle.dumps(data)
print(byte_stream)  # Output: b'\x80\x04\x95...\x94.' (binary data)

# --- DESERIALIZATION (Unpickling) ---
# Convert binary bytes back into a Python object
loaded_data = pickle.loads(byte_stream)
