# One Time Pad
This program takes a ASCII formatted message and encrypts/decrypts it using a one time pad.
### Use
This was written for Python 3 and takes 3 arguments
`python3 onetimepad.py control message pad`
- `control` must be either "encrypt" or "decrypt" (without quotes).
- `message` is the message file to be encrypted or decrypted (e.g. message.txt).
- `pad` is the one time pad to be used for encryption and decryption.
### Troubleshooting
- The pad for encrypting the message must be long enough, the amount of digits in the pad must be
three times the number of characters in the message (3 digits per ASCII character).
- This program assumes that the message and pad are ASCII formatted.
