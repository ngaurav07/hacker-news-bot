import json
def read_json(json_name):
    with open(json_name, 'r') as f:
    # Load the contents of the file into a Python object
        data = json.load(f)
    # get the already posted data
    return data
        
def append_json(json_name, hacker_news_id):
    # Append the new data to the existing data
    data = read_json(json_name)
    data['id'].append(hacker_news_id)

    # Open the JSON file for writing
    with open(json_name, 'w') as f:
        # Write the updated data back to the file
        json.dump(data, f)
        
def check_if_id_in_json(json_name, hacker_news_id):
    data = read_json(json_name)
    if(hacker_news_id in data['id']):
        return True
    return False

