import os
import subprocess
import pyscreenrec
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SCREENSHOT_DIR = "screenshots"
VIDEO_DIR = "videos"
recorder = pyscreenrec.ScreenRecorder()
SCREEN_INDEX = "1"

@pytest.fixture(scope="session", autouse=True)
def create_dirs():
    for folder in ["reports", "screenshots", "gifs","videos"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

def start_ffmpeg_recording(output_path):
    SCREEN_INDEX = "2"  # Capture screen 0 (the entire screen) on macOS avfoundation
    command = [
        "ffmpeg",
        "-y",
        "-f", "avfoundation",
        "-framerate", "15",
        "-video_size", "3024x1964",
        "-i", SCREEN_INDEX,
        "-vcodec", "libx264",
        "-pix_fmt", "yuv420p",
        output_path
    ]
    print(f"Starting FFmpeg with command: {' '.join(command)}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process


@pytest.fixture(scope="session", autouse=True)
def screen_recorder():

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.abspath(os.path.join(VIDEO_DIR, f"full_test_run_{timestamp}.mp4"))
    print(f"Screen recording output set to: {output_file}")

    ffmpeg_process = start_ffmpeg_recording(output_file)
    yield
    print("Stopping FFmpeg process...")
    ffmpeg_process.terminate()
    try:
        stdout, stderr = ffmpeg_process.communicate(timeout=15)
        print("FFmpeg stdout:", stdout.decode())
        print("FFmpeg stderr:", stderr.decode())
    except subprocess.TimeoutExpired:
        print("FFmpeg did not terminate in time, killing forcibly.")
        ffmpeg_process.kill()
        stdout, stderr = ffmpeg_process.communicate()
        print("FFmpeg stdout:", stdout.decode())
        print("FFmpeg stderr:", stderr.decode())

    print(f"Screen recording saved to: {output_file}")


@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    mobile_emulation = {"deviceName": "Pixel 2"}  # Mobile emulator
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    return opts


@pytest.fixture
def driver(chrome_options):

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(8)

    yield driver
    # Stop recording and cleanup
    driver.quit()


            


