
from project_willy.methods.errors import Return, ExitFromCLI

class General:
# OPTIONS HANDLER FOR MENU
    def options_handler(self, user_command: str, options: dict) -> None:
        command = user_command.strip().lower()
        if command in options:
            options[command]()
            return True

# RETURN TO PREVIOUS OPTION
    def option_return_to_previous(self) -> None:
        raise Return

# EXIT FROM PROGRAM OPTION
    def option_exit_from_cli(self) -> None:
        raise ExitFromCLI
