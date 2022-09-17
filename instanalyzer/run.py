import json

import utils


def main() -> None:
    # get followers and following accounts
    username, password = utils.get_username_and_password()
    driver = utils.get_driver()
    utils.open_instagram(driver)
    utils.accept_cookies(driver)
    utils.login(driver, username, password)
    utils.do_not_save_login_information(driver)
    utils.turn_off_notifications(driver)
    utils.go_to_profile(driver, username)
    follower_amount, following_amount = utils.get_follower_and_following_amount(driver)
    utils.open_followers(driver, username)
    follower_set = utils.get_followers(driver, follower_amount)
    utils.open_following(driver, username)
    following_set = utils.get_following(driver, following_amount)
    driver.close()
    # compute the relevant sets
    not_following_back_set = following_set - follower_set
    not_followed_back_by_me_set = follower_set - following_set
    common_core_set = following_set.intersection(follower_set)
    with open('not_following_back_set.json', 'w') as file:
        file.write(json.dumps(list(not_following_back_set)))
    with open('not_followed_back_by_me_set.json', 'w') as file:
        file.write(json.dumps(list(not_followed_back_by_me_set)))
    with open('common_core_set.json', 'w') as file:
        file.write(json.dumps(list(common_core_set)))
    print(f'not_following_back_set: {not_following_back_set}')
    print(f'not_followed_back_by_me_set: {not_followed_back_by_me_set}')
    print(f'common_core_set: {common_core_set}')
    print('Thanks for using instanalyzer!')


if __name__ == '__main__':
    main()
