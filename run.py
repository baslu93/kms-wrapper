from flask import Flask
import os
from jwcrypto import jwk,jwe
import base64

app = Flask(__name__)

@app.route("/keys/<kid>")
def getWrappedKey(kid):
    publicKey = jwk.JWK.from_pem(bytes(os.environ['BYOK_CERT'], 'utf-8'))
    keyMaterial = os.environ['KEY_MATERIAL']
    protectedHeader = {
        "alg": "RSA-OAEP",
        "enc": "A256GCM",
        "kid": kid
    }
    jweToken = jwe.JWE(base64.b64decode(keyMaterial.encode('utf-8')), recipient = publicKey, protected = protectedHeader)
    return {'kid': kid, 'jwe': jweToken.serialize(True)}