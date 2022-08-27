import os
import time
import tap

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

XPATH_CONSTANTS = {'accept_cookies_button': '/html/body/div[4]/div/div/button[1]',
                   'username_input': '/html/body/div[1]/section/main/article/div[2]/'
                                     'div[1]/div[2]/form/div/div[1]/div/label/input',
                   'password_input': '/html/body/div[1]/section/main/article/div[2]/'
                                     'div[1]/div[2]/form/div/div[2]/div/label/input',
                   'login_button': '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]',
                   'do_not_save_login_information_button': '/html/body/div[1]/section/main/div/div/div/div/button',
                   'turn_off_notifications_button': '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/'
                                                    'div/div/div/div/div[2]/div/div/div[3]/button[2]',
                   'open_followers_button': '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                            'section/main/div/header/section/ul/li[2]/a/div',
                   'follower_count': '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                     'section/main/div/header/section/ul/li[2]/a/div/span',
                   'following_count': '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                      'section/main/div/header/section/ul/li[3]/a/div/span'}


class ScriptArgumentParser(tap.Tap):
    username: str = os.getenv('INSTAGRAM_USERNAME', '')
    password: str = os.getenv('INSTAGRAM_PASSWORD', '')


def get_username_and_password() -> tuple[str, str]:
    args = ScriptArgumentParser().parse_args()
    return args.username, args.password


def get_driver() -> Chrome:
    return Chrome()


def send_keys_with_wait(element: WebElement, text: str, wait_time: float = 1) -> None:
    element.send_keys(text)
    time.sleep(wait_time)


def open_instagram(driver: Chrome) -> None:
    driver.get('https://www.instagram.com')


def get_element(driver: Chrome, xpath_constants_key: str, timeout: float = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_element_located((By.XPATH, XPATH_CONSTANTS[xpath_constants_key])))


def accept_cookies(driver: Chrome) -> None:
    accept_cookies_button = get_element(driver, 'accept_cookies_button')
    accept_cookies_button.click()


def login(driver: Chrome, username: str, password: str) -> None:
    username_input = get_element(driver, 'username_input')
    send_keys_with_wait(username_input, username)
    password_input = get_element(driver, 'password_input')
    send_keys_with_wait(password_input, password)
    login_button = get_element(driver, 'login_button')
    login_button.click()


def do_not_save_login_information(driver: Chrome) -> None:
    do_not_save_login_information_button = get_element(driver, 'do_not_save_login_information_button')
    do_not_save_login_information_button.click()


def turn_off_notifications(driver: Chrome) -> None:
    turn_off_notifications_button = get_element(driver, 'turn_off_notifications_button')
    turn_off_notifications_button.click()


def go_to_profile(driver: Chrome, username: str) -> None:
    driver.get(f'https://www.instagram.com/{username}/')


def get_follower_and_following_amount(driver: Chrome) -> tuple[int, int]:
    follower_count = get_element(driver, 'follower_count')
    following_count = get_element(driver, 'following_count')
    return 0, 0


def open_followers(driver: Chrome):
    open_followers_button = get_element(driver, 'open_followers_button')
    open_followers_button.click()
