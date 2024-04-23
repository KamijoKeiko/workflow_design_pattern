from request_json import apply_a, apply_b

from command_pattern import WorkflowCommander
from state_pattern import WorkflowContext


def main():

    WorkflowCommander().execute(apply_a)

    WorkflowContext().run(apply_b)


if __name__ == "__main__":
    main()


