# CPN Hammer

## Running Bidder endpoint

To run openRTB bidder endpoint you can use the following command <br>
`python3 cli/Server.py run  [--port=<number>]`

if `--port` is not specified, `9000` is used.

#### Custom environment
We also provide a bash wrapper to launch the RTB bidder using custom python environment 
<br>
`./rtb_bidder.sh [--port=<number>]`

This wrapper uses content of the `~/.site-packages.env` file to identify the location of `site-packages` you want to use.

Before using the wrapper you need to initialize this file with the right path <br>

`echo "<your path to site/user packages>" > ~/.site-packages.env`

#### Example
`echo "~/venv3/lib/python3.7/site-packages/" > ~/.site-packages.env`

## The easiest way to get started with the RTB bidder
```shell script
pip3 install fire
python3 cli/Server.py run
```

## Example
### Request
```shell script
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
```

## Dependencies
If you just need to run the bidder endpoint w/o generating images of ads served the only dependency is `fire` <br>


