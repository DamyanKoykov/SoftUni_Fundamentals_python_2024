class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return (f"{self.sender} says to {self.receiver}:"
                f" {self.content}. Sent: {self.is_sent}")


mailbox = []
while True:
    command = input().split()

    if "Stop" in command:
        break

    else:
        sender_ = command[0]
        receiver_ = command[1]
        content_ = command[2]
        email = Email(sender_, receiver_, content_)
        mailbox.append(email)

send_emails = list(map(int, input().split(", ")))
for index in send_emails:
    mailbox[index].send()

for current_email in mailbox:
    print(current_email.get_info())
