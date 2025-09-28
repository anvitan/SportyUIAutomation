import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TwitchHome:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        time.sleep(5)

    def open_home(self):
        self.driver.get("https://www.twitch.tv/")
        time.sleep(5)

    def open_search(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Layout-sc-1xcs6mc-0 kqfUha']//a[@href='/directory']")))
        btn.click()
        time.sleep(5)

    def search(self, text):
        inp = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
        inp.send_keys(text)
        inp.send_keys(Keys.ENTER)

    def scroll_down(self, times=2):
        for i in range(times):
            before = self.driver.execute_script("return window.pageYOffset;")
            print(f"Before scroll {i+1}: {before}")

            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

            after = self.driver.execute_script("return window.pageYOffset;")
            time.sleep(10)
            print(f"After scroll {i+1}: {after}")

    def get_first_stream_card_and_click(self):
        cards = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='Layout-sc-1xcs6mc-0 fhdcVy shelfItems--cfo97']/div/button[1]")))
        cards[0].click()
        time.sleep(10)

    def handle_possible_modal(self,timeout=5):
        try:
            close = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-close, .close, .close-btn"))
            )

            close.click()
        except Exception:
            # no modal appeared, safe to continue
            pass

    def wait_until_streamer_page_loads(self):
        wait = WebDriverWait(self.driver, 25)

        # Wait for video player
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-a-target='video-player']")
        ))

        # Wait for chat input (Send a message box)
        wait.until(EC.presence_of_element_located(
             (By.CSS_SELECTOR, "div[data-a-target='chat-input']")
         ))
        time.sleep(10)
        print("Streamer page fully loaded with video + chat.")