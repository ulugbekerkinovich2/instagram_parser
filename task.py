from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
username_ = input('input your username instagram>>> ')
password_ = input('input your password instagram>>> ')
input_url = input('input url from instagram>>> ')

login_url = 'https://www.instagram.com/accounts/login/'


def get_source_html(url):
    driver.maximize_window()
    # print('ishladi')
    try:
        driver.get(login_url)
        time.sleep(4)
        username = driver.find_element(By.NAME, 'username')
        # print(username_)
        time.sleep(2)
        username.send_keys(str(username_).strip())
        time.sleep(2)
        password = driver.find_element(By.NAME, 'password')
        password.send_keys(str(password_).strip())
        # print(password_)
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        time.sleep(3)
        for button in buttons:
            if 'Log in' in button.text:
                button.click()
                break
        time.sleep(5)
        driver.get(url)
        time.sleep(1)
        while True:
            try:
                by_scroll = driver.find_element(By.CLASS_NAME, '_abl-')  # _a9ym  _a9zr
                driver.execute_script("arguments[0].scrollIntoView();", by_scroll)
                time.sleep(1)
                scroll = driver.find_element(By.CLASS_NAME, '_aaqw')
                driver.execute_script("arguments[0].scrollIntoView();", scroll)
                break
            except Exception as ex:
                print(ex)
                break
        elements = driver.find_elements(By.CLASS_NAME, '_a9ym')
        for element in elements:
            text = element.text.strip()
            if text:
                # print(text, '\n')
                if 'View replies' in text:
                    # print('✅', text, '✅', '\n')
                    replies = element.find_element(By.CLASS_NAME, '_a9yg')
                    replies.click()
        for element in elements:
            # print(element.text.strip().split('\n'), '\n')
            username_instagram = element.find_element(By.CLASS_NAME, 'xt0psk2').text
            message_instagram = element.find_element(By.CLASS_NAME, '_a9zs').text
            datetime_ = element.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
            datetime_obj = datetime.strptime(datetime_, '%Y-%m-%dT%H:%M:%S.%fZ')
            likes_count = element.find_element(By.TAG_NAME, 'button').text
            if not likes_count.split(' ')[0].isdigit():
                likes_count = 'mavjud emas'
            # video_url = driver.find_element(By.CLASS_NAME, 'x1lliihq').get_attribute('src')
            # try:
            #     print('VIDEO_URL: ', video_url, '\n')
            # except:
            #     print(' ')
            print("\tUSERNAME_INSTAGRAM>>> ", username_instagram, '\n\tMESSAGE_INSATGRAM>>> ', message_instagram)
            print("\tMESSAGE_DATETIME>>> ", datetime_obj)
            print("\tLIKES>>> ", likes_count, '\n')
            for el in element.find_elements(By.CLASS_NAME, '_a9yo'):
                text = el.text
                # print('\t\t', text.strip().split('\n'), '\n')

                sub_datas = el.find_elements(By.CLASS_NAME, '_a9zr')
                for sub_data in sub_datas:
                    sub_username_instagram_from = sub_data.find_element(By.CLASS_NAME, 'xt0psk2').text
                    try:
                        sub_username_instagram_to = sub_data.find_element(By.CLASS_NAME, '_a9zs').find_element(
                            By.TAG_NAME, 'a').text
                        if sub_username_instagram_to:
                            sub_username_instagram_message = sub_data.find_element(By.CLASS_NAME, '_aacl').text
                            filter_text = ' '.join(sub_username_instagram_message.split(' ')[1:])
                            datetime_ = sub_data.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                            datetime_obj = datetime.strptime(datetime_, '%Y-%m-%dT%H:%M:%S.%fZ')
                            print(f'\t\tFROM->  {sub_username_instagram_from} to-> {sub_username_instagram_to}')
                            print(f"\t\tMESSAGE -> {filter_text}")
                            print(f"\t\tDATETIME -> {datetime_obj}\n")
                    except:
                        sub_username_instagram_message = sub_data.find_element(By.CLASS_NAME, '_a9zs').find_element(
                            By.TAG_NAME, 'span').text
                        datetime_ = sub_data.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                        datetime_obj = datetime.strptime(datetime_, '%Y-%m-%dT%H:%M:%S.%fZ')
                        print(f'\t\tFROM->  {sub_username_instagram_from} message-> {sub_username_instagram_message}')
                        print(f'\t\tDATETIME -> {datetime_obj}\n')
        # time.sleep(2000)
    except Exception as ex:
        print(ex)
        time.sleep(500000)
        driver.close()
        driver.quit()


def main():
    get_source_html(url=input_url)


if __name__ == '__main__':
    main()
