import threading

# Send emails asynchronously
class EmailThread(threading.Thread):
    def __init__(self, msg):
        self.msg = msg
        threading.Thread.__init__(self)

    def run (self):
        self.msg.send(fail_silently=True)

def send_async_mail(msg, *args, **kwargs):
    EmailThread(msg).start()

