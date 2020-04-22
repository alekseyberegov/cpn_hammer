#!/bin/bash

curl --location --request POST 'http://localhost:9000' \
--header 'Content-Type: application/json' \
--header 'Host: localhost' \
--header 'x-openrtb-version: 2.5' \
--data-raw '{
    "id" : "fffd894f-c33c-4c08-b826-4448fcaecc85",
    "bcat" : [ "CTX-1", "CTX-3", "CTX-4" ],
    "imp": [
        {
        "id": "aaad894f-c33c-4c08-b826-4448fcaecc899",
         "instl": 1
        }
    ],
    "site": {
        "id": "19283",
        "cat" : [ "IAB12", "IAB12-5" ]
    },
    "device": {
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "ip": "108.185.178.0"
    },
    "user": {
        "id": "08057c4b-4cb3-4e65-8a9b-b6db49d921a7"
    }
}'

echo ""