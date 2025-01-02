import instagrapi.types
import os
import tap


class ScriptArgumentParser(tap.Tap):
    username: str = os.getenv("INSTAGRAM_USERNAME", "")
    password: str = os.getenv("INSTAGRAM_PASSWORD", "")


def get_username_and_password() -> tuple[str, str]:
    args = ScriptArgumentParser().parse_args()
    return args.username, args.password


def get_username(user: instagrapi.types.UserShort) -> str:
    username: str | None = user.username
    if username is None:
        raise RuntimeError
    return username
