import os, time
from pages.twitch_home import TwitchHome

def test_twitch_mobile_flow_and_screenshot(driver):
    home = TwitchHome(driver)
    home.open_home()
    home.open_search()
    home.search("StarCraft II")
    home.scroll_down(2)
    home.get_first_stream_card_and_click()
    home.handle_possible_modal()
    home.wait_until_streamer_page_loads()

    os.makedirs("screenshots", exist_ok=True)
    filename = f"screenshots/streamer_{int(time.time())}.png"
    driver.save_screenshot(filename)
    assert os.path.exists(filename)


