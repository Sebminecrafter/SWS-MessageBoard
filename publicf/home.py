def main(req):
    output = """<!DOCTYPE html>
    <html>
        <head>
            <title>Messageboard</title>
        </head>
        <body>
            <h1>Messageboard</h1>
            <h2>Post a message</h2>
            <form action="/post" method="GET">
                <label for="name">Enter your name: </label>
                <input type="text" name="name" required />
                <label for="msg">Enter your message: </label>
                <input type="text" name="msg" required />
                <input type="submit" value="Post" />
            </form>
            <h2>Messages</h2>
            <CONTENT/>
        </body>
    </html>"""
    content = "<pre>"
    try:
        namesf = open("names.txt", 'r')
        msgsf = open("msgs.txt", 'r')
        names = namesf.readlines()
        msgs = msgsf.readlines()
        namesf.close()
        msgsf.close()
        for i in range(len(names)):
            content += f"<b>{names[i]}</b>\n{msgs[i]}\n"
    except OSError:
        content += "No messages."
    content += "</pre>"
    output = output.replace("<CONTENT/>", content)
    status = 200
    otype = 'text/html'
    return output, status, otype