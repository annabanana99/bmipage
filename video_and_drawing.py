from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class HTML5VideoPlayer(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(
            "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver = webdriver.Firefox(firefox_binary=binary)


    @unittest.skip
    def test_video(self):

        self.driver.get("https://www.w3schools.com/html/html5_video.asp")

        video_clip = self.driver.find_element_by_id("video1")

        # execute with java script
        source = self.driver.execute_script("return arguments[0].currentSrc;",
               video_clip)

        duration = self.driver.execute_script("return arguments[0].duration;",
               video_clip)

        # verify video clip length
        self.assertAlmostEqual(duration, 10, 1)

        # verify if correct video is loaded
        self.assertEqual(source, "https://www.w3schools.com/html/mov_bbb.mp4")

        # play video
        duration = self.driver.execute_script("return arguments[0].play();",
                video_clip)

        time.sleep(5)

        # pause video
        self.driver.execute_script("arguments[0].pause()", video_clip)


    def test_canvas(self):
        self.driver.get("https://drawisland.com/")
        self.driver.implicitly_wait(3)

        canvas = self.driver.find_element_by_id("im_canvas")
        tools_pencil = self.driver.find_element_by_id("pencil")
        tools_circle = self.driver.find_element_by_id("unfilled_round")
        tools_eraser = self.driver.find_element_by_id("eraser")
        delete_drawing = self.driver.find_element_by_id("delete")

        actions_builder = ActionChains(self.driver)

        actions_builder.click(tools_pencil).move_to_element(
            canvas).click_and_hold(canvas).move_by_offset(25,-10)\
            .release().perform()


        delete_drawing.click()





    def tearDown(self):
        self.driver.quit()






if __name__ == '__main__':
    unittest.main(verbosity = 2)
