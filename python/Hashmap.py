# Create an empty hashmap
hashmap = {}

# Insert key-value pairs
hashmap["key1"] = "value1"
hashmap["key2"] = "value2"
hashmap["key3"] = "value3"

# Access values by key
value = hashmap["key1"]
print(f"Value for key1: {value}")

# Check if a key exists in the hashmap
if "key2" in hashmap:
    print("key2 exists in the hashmap")

# Delete a key-value pair
del hashmap["key3"]

# Iterate over the keys and values
for key, value in hashmap.items():
    print(f"Key: {key}, Value: {value}")
