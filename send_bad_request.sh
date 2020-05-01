#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -h|--help)
    echo ""
    echo "Usage: $0 [-c|--count <request count>] [-e|--endpoint <endpoint>]"
    exit 1
    ;;
    -c|--count)
    COUNT="$2"
    shift # past argument
    shift # past value
    ;;
    -e|--endpoint)
    ENDPOINT="$2"
    shift # past argument
    shift # past value
    ;;
    --default)
    DEFAULT=YES
    shift # past argument
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

COUNT=${COUNT:-1}
ENDPOINT=${ENDPOINT:-"http://127.0.0.1:9000"}

for i in `eval echo {1..$COUNT}`
do
  curl --location --request POST ${ENDPOINT} \
  --header 'Content-Type: application/json' \
  --header 'Host: localhost' \
  --header 'x-openrtb-version: 2.5' \
  --data-raw '{
      "id" : "fffd894f-c33c-4c08-b826-4448fcaecc85",
      "bcat" : [ "CTX-1", "CTX-3", "CTX-4" ],
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
done
