class MailSenderMixin:

    def send_mail(self, to, body):
        print(f"メールを送信: {to}, {body}")