# CPN Hammer

### Running Bidder endpoint

To run openRTB bidder endpoint you can use the following command <br>
`python3 cli/Server.py run`

However, because there a few dependencies that should be in `PYTHONPATH` we provide a shell wrapper to launch the RTB bidder<br>
`./rtb_bidder.sh [--port=<number>]`

if `--port` is not specified, `9000` is used.

This wrapper needs to know the directory where modules are located. To find them it uses the content of the file:
`~/.site-packages.env`

You need to initialize this file with something like:<br>

`echo "~/venv3/lib/python3.7/site-packages/" > ~/.site-packages.env`

The path `~/venv3/lib/python3.7/site-packages/` is setup specific; so, please use the one that is applicable to your environmentt


## Dependencies
If you just need to run the bidder endpoint w/o generating images of ads served the only dependency is `fire`
