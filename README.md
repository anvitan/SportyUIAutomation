git clone [<your-ui-repo-url>](https://github.com/anvitan/SportyUIAutomation.git)
cd home-test-ui

2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate  

3. Install dependencies
pip install -r requirements.txt

▶️ Running Tests
 pytest test/twitch_test.py --html=reports/report.html --self-contained-html -v -s

Project Structure

twitch-ui-automation/

├── pages  
│└── twitch_home.py # Browser drivers like chromedriver│
├── tests/
│└── twitch_test.py# Contains the mobile emulator test case
││└── conftest.py # to set pre condition
├── requirements.txt                    # Python dependencies
└── README.md                          # Project overview and usage

After running test it will generate screenshots/reports and video of the automation results

📱 Test Case – Twitch Flow

Steps automated:

Open Twitch in mobile emulator (Pixel 2).

Click the search icon.

Enter StarCraft II.

Scroll down twice.

Select the first streamer.

Handle modal/popup if it appears.

Wait until streamer page fully loads.

Capture a screenshot.

✅ Screenshot saved in the screenshots/ folder.

Video will be recorded 

✅ Videos saved in the videos/ folder.

Reports will be added in 

✅ Reports saved in the reports/ folder.