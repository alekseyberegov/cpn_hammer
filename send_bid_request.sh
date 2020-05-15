#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -h|--help)
    echo ""
    echo "Usage: $0 [-c|--count <request count>] [-e|--endpoint <endpoint>] [-d|--debug] [--silent]"
    exit 1
    ;;
    -c|--count)
    count="$2"
    shift # past argument
    shift # past value
    ;;
    -e|--endpoint)
    endpoint="$2"
    shift # past argument
    shift # past value
    ;;
    -d|--debug)
    debug="TRUE"
    shift # past argument
    ;;
    --silent)
    silent=" -silent --output /dev/null "
    shift # past argument
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

count=${count:-1}
endpoint=${endpoint:-"http://127.0.0.1:9000"}

#hdr_host_name=$(echo $endpoint | awk -F[/:] '{print $4}')
proto="$(echo ${endpoint} | grep :// | sed -e's,^\(.*://\).*,\1,g')"
url="$(echo ${endpoint/$proto/})"
hdr_host_name="$(echo ${url} | cut -d/ -f1)"
hdr_cont_type="Content-Type: application/json"
hdr_open_rtb="x-openrtb-version: 2.5"

dev_ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
dev_ip="108.185.179.0"
pub_id="2949"
pub_cat="[\"sport\", \"coats\", \"spring\"]"

if [[ "$debug" = "TRUE" ]]
then
  echo ""
  echo "silent   = ${silent}"
  echo "count    = ${count}"
  echo "endpoint = ${endpoint}"
  echo "content  = ${hdr_cont_type}"
  echo "host     = ${hdr_host_name}"
  echo "rtb      = ${hdr_open_rtb}"
  echo ""
fi

for i in `eval echo {1..$count}`
do
  req_id=$(uuidgen)
  usr_id=$(uuidgen)

  curl $silent --location --request POST ${endpoint} \
  --header "${hdr_cont_type}" \
  --header "${hdr_host_name}" \
  --header "${hdr_open_rtb}" \
  --data-raw "{
      \"id\" : \"${req_id}\",
      \"bcat\" : [],
      \"imp\": [
          {
          \"id\": \"${req_id}\",
          \"instl\": 1
          }
      ],
      \"site\": {
          \"id\": \"${pub_id}\",
          \"cat\" : ${pub_cat}
      },
      \"device\": {
          \"ua\": \"${dev_ua}\",
          \"ip\": \"${dev_ip}\"
      },
      \"user\": {
          \"id\": \"${usr_id}\"
      }
  }"
  if [[ "$silent" = "" ]]
  then
    echo ""
  fi
done
