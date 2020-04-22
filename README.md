# CPN Hammer

## Running Bidder endpoint

To run openRTB bidder endpoint you can use the following command <br>
`python3 cli/Server.py run  [--port=<number>]`

We also provide a shell wrapper to launch the RTB bidder, which allows to use specific python environment 
(important in case of multiple Python virtual environments)<br>
`./rtb_bidder.sh [--port=<number>]`

if `--port` is not specified, `9000` is used.

This wrapper needs to know the location of `site-packages` that you want to use.  You can use `~/.site-packages.env`
to specify the location

You need to initialize this file with a path to `site-packages`<br>

`echo "~/venv3/lib/python3.7/site-packages/" > ~/.site-packages.env`

The path `~/venv3/lib/python3.7/site-packages/` is setup specific; so, please use the one that is applicable to your environment

## Example
### Request
`POST http://localhost:9000` <br>
```javascript
{
    "id": "5c33cff4-7487-11ea-a415-f2189846117c", 
    "bcat": ["IAB-23", "IAB-24", "IAB-25", "IAB-26"], 
    "imp": [{
        "id": "5c33d166-7487-11ea-a415-f2189846117c", 
        "instl": 1
        }], 
    "site": {
        "id": "1482", 
        "cat": ["IAB2-18", "Pickup", "Automotive"
        ]}, 
    "user": {"id": "5c33d382-7487-11ea-a415-f2189846117c"}, 
    "device": {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36", 
        "ip": "199.248.234.0"
        }
}
```

## Dependencies
If you just need to run the bidder endpoint w/o generating images of ads served the only dependency is `fire`
