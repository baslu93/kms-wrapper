# kms-wrapper

This Rest API returns a valid response for Salesforce Bring Your Own Key (BYOK) Cache-Only.
No matter what the KID will be, it will always return the same key material.

__Don't use this in Production Environments__, the purpose of this implementation is to create a valid key wrapper tool and to monitor how often a key is retrived by Salesforce.

Look at the Swagger [here](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/baslu93/ksm-wrapper/main/swagger.json).

## Pre-deploy steps

Before deploying this on Heroku, you need to perform several tasks on Salesforce:
- Create the BYOK 4096 Certificate
    - Be sure to have the "Manage Encryption Keys" permission
    - Write "Certificate" in the Quick find box in Setup
    - Click on "Create Self-Signed Certificate"
    - Create your certificate:
        - Set "Key Size" to 4096
        - Set "Exportable Private Key" to false
        - set "Use Platform Encryption" to true
- Create the key material
    - Write the following script in Developer Console, and get the result:
        ```
        Blob key = Crypto.generateAesKey(256);
        String base64key = EncodingUtil.base64Encode(key);
        System.debug('Base64(key): ' + base64key);
        ```

## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/baslu93/kms-wrapper)

## Next steps

- [x] Create a valid wrapper
- [ ] Implement an Authentication Protocol (JWT based) 
- [ ] Add Replay Detection for Cache-Only Keys

## Evidence

Work in progress, stay tuned!
