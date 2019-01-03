# -*- coding: utf-8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Tplink(object):

    def __init__(self, url, username, password):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.url = "url"
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),
                                       chrome_options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.username = self.driver.find_element_by_id("cloud-login-username")
        self.username.send_keys(username)
        self.password = self.driver.find_element_by_xpath("//input[@type='password']")
        self.password.send_keys(password)
        self.password.send_keys(Keys.ENTER)

    def internet_menu(self):
        time.sleep(15)
        internet_menu = self.driver.find_element_by_id("menu-basic-internet-li")
        internet_menu.click()
        time.sleep(2)
        dropdown = self.driver.find_element_by_id("ip-setting")
        dropdown.click()

    def vpn_off(self):
        self.internet_menu()
        item = self.driver.find_element_by_xpath("(//label[@type='single'])[28]")
        item.click()
        save = self.driver.find_element_by_xpath("(//button[@type='button'])[2]")
        time.sleep(2)
        save.click()

    def vpn_on(self):
        self.internet_menu()
        item = self.driver.find_element_by_xpath("(//label[@type='single'])[30]")
        item.click()
        save = self.driver.find_element_by_xpath("//button[@id='l2tp_total_save']")
        time.sleep(2)
        save.click()
