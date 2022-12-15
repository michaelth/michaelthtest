import hashlib
import binascii

def process_request(request):
    password = request.GET["password"]

    # BAD: Inbound authentication made by comparison to string literal
    if password == "myPa55word":
        redirect("login")

    hashed_password = load_from_config('hashed_password', CONFIG_FILE)
    salt = load_from_config('salt', CONFIG_FILE)