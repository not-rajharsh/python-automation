import logging
import hashlib
import time
import requests

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
)

# Use a static endpoint
url = "https://httpbin.org/get"

while True:
    response1 = requests.get(url)
    hash_object1 = hashlib.sha256(response1.text.encode())
    hex_digest1 = hash_object1.hexdigest()

    time.sleep(10)

    response2 = requests.get(url)
    hash_object2 = hashlib.sha256(response2.text.encode())
    hex_digest2 = hash_object2.hexdigest()

    if hex_digest1 == hex_digest2:
        logging.debug('No Change')
    else:
        logging.debug('Change Detected!')