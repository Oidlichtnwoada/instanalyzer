import utils


def main() -> None:
    username, password = utils.get_username_and_password()
    driver = utils.get_driver()
    utils.open_instagram(driver)
    utils.accept_cookies(driver)
    utils.login(driver, username, password)
    utils.do_not_save_login_information(driver)
    utils.turn_off_notifications(driver)
    utils.go_to_profile(driver, username)
    follower_count, following_count = utils.get_follower_and_following_amount(driver)
    utils.open_followers(driver)
    driver.close()


if __name__ == '__main__':
    main()
