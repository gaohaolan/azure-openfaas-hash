import azure.functions as func
import logging
import hashlib

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HashPython")
def HashPython(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get 'text' 
    text = req.params.get('text')
    
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    # error
    if not text:
        return func.HttpResponse(
            "Please provide a 'text' parameter in the query string or in the request body.",
            status_code=400
        )

    # calculate SHA-256 value
    hash_object = hashlib.sha256(text.encode('utf-8'))
    hash_hex = hash_object.hexdigest()

    return func.HttpResponse(
        f"SHA-256 Hash for '{text}' is: {hash_hex}",
        status_code=200
    )