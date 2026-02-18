import json
import pathlib


def get_data_base_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent / "data"

def get_followers() -> set[str]:
    with open(get_data_base_path() / "followers_1.json") as file:
        data = json.load(file)
    ids = set([x["string_list_data"][0]["value"] for x in data])
    return ids


def get_followings() -> set[str]:
    with open(get_data_base_path() / "following.json") as file:
        data = json.load(file)
    ids = set([x["title"] for x in data["relationships_following"]])
    return ids

def main() -> None:
    followers = get_followers()
    followings = get_followings()
    not_following_back = followings - followers
    not_followed_back = followers - followings
    common_core = followers & followings
    print(f"not following back: {not_following_back}")
    print(f"not followed back: {not_followed_back}")
    print(f"common core: {common_core}")


if __name__ == "__main__":
    main()
