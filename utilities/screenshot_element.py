from PIL import Image
from selenium import webdriver
import math
from io import StringIO

class Screenshots():
    def capture_element(driver, element):
        screenshot = driver.save_screenshot("screenshot0.png")


        size_element = element.size()

        location_y = int(size_element["y"])
        location_x = int(size_element["x"])

        width_element = int(size_element["width"])
        height_element = int(size_element["height"])

        right = location_x + width_element
        bottom = location_y + height_element

        cropped_image = screenshot.crop(location_x, location_y, right, bottom)
        cropped_image.save("screenshot.png")


