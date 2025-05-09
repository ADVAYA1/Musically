# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHomeUI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homeUI(self):
    self.driver.get("https://checkout.stripe.com/c/pay/cs_test_b1Xk4nAHUAbHSdYjm1ZWG3dSuxFsiBELHcClufj0MUpO0GmroI0t2v8T0J#fidkdWxOYHwnPyd1blpxYHZxWjA0VTFrNkhWQTVhUEZDd3dsdU9TRmswPFc0N2hdUE5LdFNETjRsRG9tVlBuZHY2fDR0S1B2a0pBbzJoR1ZSQHcxTEt%2FNz1nTENOSkZQajVPYnRncWZ%2FT0pPNTUzYmlQUzxTSScpJ2hsYXYnP34nYnBsYSc%2FJzc3N2E3NGcyKGc2PTEoMTIyNCg9YGNgKGBjMjBkZmMyM2NhYGY3Yz0yNycpJ2hwbGEnPycwMDJgYT1nMCg1MzA3KDE2MjMoPWc0NyhjNjY8Z2dnZDxgZGE1YWMyN2AnKSd2bGEnPydmMGMzYTw1Nyg9PDxkKDEzN2EoZDZhNShmNmYxYGA2MDY1MzcxNj09ZGYneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8naHBpcWxabHFgaCcpJ3dgY2B3d2B3SndsYmxrJz8nbXFxdT8qKmlqZmRpbWp2cT82NTU1J3gl/")
    self.driver.set_window_size(1536, 816)
    element = self.driver.find_element(By.CSS_SELECTOR, ".bg-neutral-100\\/10")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Search").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-neutral-700").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-neutral-700").send_keys("Kar")
    self.driver.find_element(By.CSS_SELECTOR, ".flex-1 .text-neutral-400").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-neutral-400:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".hover\\3Atext-white:nth-child(1) > path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-10:nth-child(2) path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-neutral-400 > .truncate").click()
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) .object-cover").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-neutral-400:nth-child(3) > path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".absolute:nth-child(1)").click()
  
