import unittest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select
from ddt import ddt, unpack, data

@ddt
class BMICalcDDT(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(
            "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        url = "https://www.thecalculatorsite.com/health/bmicalculator.php"
        self.driver.get(url)


    @data(("female", "no", "168", "55"),
          ("male", "yes", "182", "75"))
    @unpack
    def test_inputs(self, gender, body_is_athletic, height, weight):
        #make sure metric is selected
        self.driver.find_element_by_link_text("Metric BMI Calculator").click()

        gender_field = self.driver.find_element_by_id("gender1")
        selection_gend = Select(gender_field).select_by_value(gender)

        body_type_field = self.driver.find_element_by_id("athletic1")
        selection_body = Select(body_type_field).select_by_value(
            body_is_athletic)

        height_field = self.driver.find_element_by_id("height")
        height_field.send_keys(height)

        weight_field = self.driver.find_element_by_id("weight")
        weight_field.send_keys(weight)

        self.driver.find_element_by_name("formsubmit1").click()

        result = self.driver.find_element_by_id("gauge-result")

        if gender == "female":
            self.assertEqual(result.text, "19.49")

        if gender == "male":
            self.assertEqual(result.text, "22.64")




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


