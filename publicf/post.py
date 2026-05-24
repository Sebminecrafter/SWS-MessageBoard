import html
from urllib.parse import urlparse, parse_qs
def main(req):
    items = parse_qs(urlparse(req.path).query)
    name = html.escape(items['name'][0])
    msg = html.escape(items['msg'][0])
    with open("names.txt", 'a') as names:
        names.write(name+'\n')
    with open("msgs.txt", 'a') as msgs:
        msgs.write(msg+'\n')
    output = "<meta http-equiv=\"refresh\" content=\"0; url=/home\">"
    status = 201
    otype = 'text/html'
    return output, status, otype