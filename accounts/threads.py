import threading

from django.core.mail import EmailMessage


class SendEmailThread(threading.Thread):
    def __init__(self, email: EmailMessage):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
