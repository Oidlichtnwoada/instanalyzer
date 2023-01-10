import instagrapi.types
import tap
import os


class ScriptArgumentParser(tap.Tap):
    username: str = os.getenv('INSTAGRAM_USERNAME', '')
    password: str = os.getenv('INSTAGRAM_PASSWORD', '')


def get_username_and_password() -> tuple[str, str]:
    args = ScriptArgumentParser().parse_args()
    return args.username, args.password


def get_username(user: instagrapi.types.UserShort) -> str:
    return user.username
