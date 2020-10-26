from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import wget


def fill_field(driver, id, value):
    driver.find_element_by_id(id).clear()
    driver.find_element_by_id(id).send_keys(value)


def wait_for_result_link(driver, id):
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, id)))

    responseLinkElement = driver.find_element_by_id(id)

    return responseLinkElement.get_attribute('href')


url = 'http://www.soda-pro.com/web-services/meteo-data/merra'
driver = webdriver.Chrome('/home/vaidehee/Downloads/chromedriver')
driver.get(url)

buttonId = "ext-gen70"
formInputIds = ["latId",
                "lonId",
                "dateBegin",
                "dateEnd"]

# Put the following in a for loop for all districts
values = {
    "latId": "23",
    "lonId": "58",
    "dateBegin": "2020-04-01",
    "dateEnd": "2020-05-01"
}

district = "sample"

for id in formInputIds[:4]:
    fill_field(driver, id, values[id])

driver.execute_script(
    "document.getElementById('summarizationCode').value = 'd';")

driver.find_element_by_id(buttonId).click()


resultLink = wait_for_result_link(driver, "responseLink")
wget.download(resultLink, "./datasets/{}_weather.csv".format(district))
