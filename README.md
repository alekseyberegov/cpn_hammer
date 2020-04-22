# CPN Hammer

### Running Bidder endpoint

To run openRTB bidder endpoint use the following
python cli/Server.py run

Because there a few dependencies for this application there a shell wrapper<br>
`rtb_bidder.sh`

This wrapper needs to know the directory where modules are located. To find them it uses the file:
`~/.site-packages.env`

You need to initialize this file with something like:<br<

`echo "./venv3/lib/python3.7/site-packages/" > ~/.site-packages.env`




## Useful links
* ftp://ftp.arin.net/pub/stats/arin/
* https://docs.python.org/3/library/sqlite3.html
* https://requests.readthedocs.io/en/master/

