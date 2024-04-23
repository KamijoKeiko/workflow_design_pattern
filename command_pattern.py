from mail_sender import MailSenderMixin


class Command:
    def __init__(self, data):
        self.data = data

    def create_request(self):
        print(f"申請共通のrequest bodyを生成: {self.data['base_info']['apply_type']}")


class ApplyACommand(Command, MailSenderMixin):
    """apply_aはメール送信も必要なイメージ"""

    def create_request(self):
        super().create_request()
        print(f"Apply A 用のrequest bodyを生成: {self.data['apply_a']}")

        self.send_mail("alice@example.com", "Hello, Alice!")


class ApplyBCommand(Command):
    """apply_bはメール送信が不要なイメージ"""

    def create_request(self):
        super().create_request()

        print(f"Apply B 用のrequest bodyを生成: {self.data['apply_b']}")


class ApplyCCommand(Command):

    def create_request(self):
        super().create_request()
        print(f"Apply C 用の request bodyを生成: {self.data['apply_c']}")


class WorkflowCommander:
    def __init__(self):
        self.command_map = {
            "apply_a": ApplyACommand,
            "apply_b": ApplyBCommand,
            "apply_c": ApplyCCommand
        }

    def execute(self, received_request):
        key = list(received_request.keys())[1]  # 便宜上のコード。実際はコンポーネントキーを受け取る
        command_class = self.command_map.get(key)
        instance = command_class(received_request)
        instance.create_request()
        # 実際はここでワークフローへのリクエストを飛ばす
        return
