from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lanqiao.cn/bootcamp/")
driver.find_element_by_css_selector('li.sign-in-btn').click()
driver.find_element_by_css_selector('input[placeholder="手机号/邮箱"').send_keys('13811745471')
driver.find_element_by_css_selector('input[placeholder="密码"').send_keys('xiaocui0')
driver.find_element_by_css_selector("button.ant-btn-primary").click()

