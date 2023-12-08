from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://shivam6862.github.io/")
print(driver.title)
print(driver.current_url)

heading = driver.find_element(By.CLASS_NAME, "_name_isxm6_47").text

about_me = [about.text for about in driver.find_elements(
    By.CLASS_NAME, "_details_174mw_47")]

languages = [lang.text for lang in driver.find_elements(
    By.CLASS_NAME, "_box_text_xlahx_131")]

platforms = [platform.text for platform in driver.find_elements(
    By.CLASS_NAME, "_book_card_qj07i_35")]

connects = [connect.text for connect in driver.find_elements(
    By.CLASS_NAME, "_text_light_1bxfy_113")]

projects = [project.text for project in driver.find_elements(
    By.CLASS_NAME, "_work_4ayvq_23")]

projct_name_with_desc = []
project_elements = driver.find_elements(By.CLASS_NAME, "_work_4ayvq_23")
print(len(project_elements))
for project_element in project_elements:
    project_name = project_element.find_element(
        By.CLASS_NAME, '_work_info_4ayvq_135').text
    print(project_name)

    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "_work_info_4ayvq_135"))).click()

        project_desc = (driver.find_element(
            By.CLASS_NAME, "_box_1rqzu_45").text).split("\n")

        projct_name_with_desc.append(
            {"project_name": project_name, "project_desc": project_desc})

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "_cross_1rqzu_147"))).click()

    except Exception as e:
        print("Click intercepted. Trying alternative method.", e)

data = {
    "heading": heading,
    "about_me": about_me,
    "languages": languages,
    "platforms": platforms,
    "projects": projects,
    "project_name_with_desc": projct_name_with_desc,
    "connects": connects
}

with open("profile_data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

print((Keys.NUMPAD7))

driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Name']").send_keys("hello")
driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("shivam@gmail.com")
driver.find_element(
    By.CSS_SELECTOR, "textarea[placeholder='Message']").send_keys("Thank for joining as a member of our community")

driver.quit()
