import utils
import instagrapi


def main() -> None:
    username, password = utils.get_username_and_password()
    client = instagrapi.Client()
    client.login(username, password, relogin=True)
    user_id = client.user_id_from_username(username)
    followers = client.user_followers_v1(user_id)
    following = client.user_following_v1(user_id)
    follower_username_set = set(map(utils.get_username, followers))
    following_username_set = set(map(utils.get_username, following))
    common_core = following_username_set.intersection(follower_username_set)
    not_following_back = following_username_set - follower_username_set
    not_followed_back = follower_username_set - following_username_set
    print(f"not following back: {not_following_back}")
    print(f"not followed back: {not_followed_back}")
    print(f"common core: {common_core}")


if __name__ == '__main__':
    main()
