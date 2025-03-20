import hashlib
import json

def handle(event, context):
    # get 'text'
    if event.method == 'GET':
        
        text = event.query.get("text")
        
        # error
        if not text:
            return {
                "statusCode": 400,
                "body": "Please provide a 'text' parameter in the query string.",
		"headers": {
                    "Content-Type": "text/plain"
                }
            }
        
    # POST 
    elif event.method == 'POST':
        
        body = event.body.strip()
        decoded_body = body.decode('utf-8')
        try:
       	    json_data = json.loads(decoded_body)
        except json.JSONDecodeError:
            return {
                 "statusCode": 400,
                 "body": "Invalid JSON data"
            }

        text = json_data.get('text', None)
    
        if not text:
           return {
               "statusCode": 400,
               "body": "Text is required"
           }

    # calculate SHA-256 value
    hash_object = hashlib.sha256(text.encode('utf-8'))
    hash_hex = hash_object.hexdigest()

    return {
        "statusCode": 200,
        "body": f"SHA-256 Hash for '{text}' is: {hash_hex}",
        "headers": {
            "Content-Type": "text/plain"
        }
    }
