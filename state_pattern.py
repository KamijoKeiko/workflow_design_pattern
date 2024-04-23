from mail_sender import MailSenderMixin


class RequestState:
    def __init__(self, data):
        self.data = data

    def create_request(self, request_data):
        print(f"申請共通のrequest bodyを生成: {self.data['base_info']['apply_type']}")


class ApplyAState(RequestState, MailSenderMixin):
    def create_request(self, request_data):
        super().create_request(request_data)
        print(f"Apply A 用のrequest bodyを生成: {request_data}")

        self.send_mail("bob@example.com", "Hello, Bob!")


class ApplyBState(RequestState):
    def create_request(self, request_data):
        super().create_request(request_data)
        print(f"Apply B 用のrequest bodyを生成: {request_data}")


class ApplyCState(RequestState):
    def create_request(self, request_data):
        super().create_request(request_data)
        print(f"Apply C 用のrequest bodyを生成: {request_data}")


class WorkflowContext:
    def __init__(self):

        self.state_map = {
            "apply_a": ApplyAState,
            "apply_b": ApplyBState,
            "apply_c": ApplyCState
        }

    def run(self, received_request):
        key = list(received_request.keys())[1]  # 便宜上のコード。実際はコンポーネントキーを受け取る
        apply = self.state_map.get(key)

        apply_instance = apply(received_request)
        apply_instance.create_request(received_request)
        return

