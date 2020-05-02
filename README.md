# CPN Hammer

## Running Bidder endpoint

To run openRTB bidder endpoint you can use the following command <br>
`python3 cli/Server.py run  [--port=<number>]`

if `--port` is not specified, `9000` is used.

#### Custom environment
We also provide a bash wrapper to launch the RTB bidder using custom python environment 
<br>
`./rtb_bidder.sh [--port=<number>]`
##### Example
`./rtb_bidder.sh --port=8080 > /var/log/rtb_bidder.log 2>&1 &`

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
### Sending 10 request 
```shell script
./send_bid_request.sh -c 10 -e http://127.0.0.1:9000
```
Use `./send_bid_request.sh --help` to get information about all supported parameters

## Troubleshooting
```shell script
sudo tcpdump  -i eth0 'tcp[13] & 2 != 0 and (dst port 9000)'
```
## Dependencies
If you just need to run the bidder endpoint w/o generating images of ads served the only dependency is `fire` <br>


