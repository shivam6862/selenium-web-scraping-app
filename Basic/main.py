from selenium import webdriver
from selenium.webdriver.common.by import By
import json

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


data = {
    "heading": heading,
    "about_me": about_me,
    "languages": languages,
    "platforms": platforms,
    "projects": projects,
    "connects": connects
}

with open("profile_data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

driver.quit()
