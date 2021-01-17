import json
import time
import sys
from pathlib import Path


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class_id = input("Enter class ID [leave it blank if you don't have one]: ")
class_password = input("Enter class Password [leave it blank if you don't have one]: ")

try:
    config_file = str(Path.home() / "daan.json")
    with open(config_file, 'r') as f:
        config_content = f.read()

    config = json.loads(config_content)

except IOError:
    print("1) azad (tj)\n2) iauctb\n3) srbiau\n4) daanaan\n5) iau-tnb\n6) iauet")
    branhes = {1: "azad", 2: "iauctb", 3: "srbiau", 4:" daanaan", 5: "iau-tnb", 6: "iauet"}
    branch_select = int(input("Select the branch: "))
    branch = branhes[branch_select]
    user_id_number = input("User ID number: ")
    user_password = input("Password: ")

    config = {"branch": branch, "user_id_number": user_id_number, "user_password": user_password}

    config_content = json.dumps(config)
    config_file = str(Path.home() / "daan.json")

    with open(config_file, 'w') as f:
        f.write(config_content)

branch = config["branch"]
user_id_number = config["user_id_number"]
user_password = config["user_password"]

base_url = "http://" + branch + ".daan.ir"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("ScreenRecorder.zip")

chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1
    })

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{base_url}/login-identification-form#login-identification-form")
assert "دان" in driver.title

id_number = driver.find_element_by_name("identification_number")
id_number.clear()
id_number.send_keys(user_id_number)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(user_password)
password.send_keys(Keys.RETURN)

time.sleep(2)

valid_session = False
while not valid_session:
    driver.get(f"{base_url}/session-list#session-list")

    if class_id and class_password:
        class_id_field = driver.find_element_by_name("id")
        class_passowrd_field = driver.find_element_by_name("password")
        class_id_field.send_keys(class_id)
        class_passowrd_field.send_keys(class_password)
        class_passowrd_field.send_keys(Keys.RETURN)
        time.sleep(5)
        alert = driver.find_elements_by_css_selector("div.alert")
        if not alert:
            valid_session = True
            sys.exit(0)

        time.sleep(10)

    else:
        sessions = driver.find_elements_by_css_selector("td>a.btn-info")

        for session in sessions:
            session_link = str(session.get_attribute("href"))
            if "enter-session" in session_link:
                valid_session = True
                driver.get(session_link)
                sys.exit(0)
        print("You don't have a class right now / Teacher doesn't entered yet")
        time.sleep(15)


# .teacher-not-entered-classroom: Not entered
# .session_not_reach: Class ended or not started
# if teacher entred, the button has a link
