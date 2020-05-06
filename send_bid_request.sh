#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -h|--help)
    echo ""
    echo "Usage: $0 [-c|--count <request count>] [-e|--endpoint <endpoint>] [--silent]"
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
    --silent)
    SILENT=" -silent --output /dev/null "
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

echo "COUNT         = ${COUNT}"
echo "ENDPOINT      = ${ENDPOINT}"
echo "SILENT        = ${SILENT}"

for i in `eval echo {1..$COUNT}`
do
  curl $SILENT --location --request POST ${ENDPOINT} \
  --header 'Content-Type: application/json' \
  --header 'Host: engine.4dsply.com' \
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
          "cat" : [ "IAB12", "IAB12-5", "coats", "spring" ]
      },
      "device": {
          "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
          "ip": "108.185.179.0"
      },
      "user": {
          "id": "08057c4b-4cb3-4e65-8a9b-b6db49d921a7"
      }
  }'
  if [[ "$SILENT" = "" ]]
  then
    echo ""
  fi
done
