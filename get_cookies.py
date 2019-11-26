from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.taobao.com/')
driver.implicitly_wait(10)
#进入登录页面
driver.find_element_by_link_text('亲，请登录').click()
#手动去扫码登录
time.sleep(10)
#获取cookies

cookies = driver.get_cookies()
print(cookies)

'''

driver.get('https://www.taobao.com')
driver.maximize_window()
cookies = [{}]
for item in cookies:
    driver.add_cookie(item)

driver.get('https://www.taobao.com')
time.sleep(5)

#driver.refresh()
'''

""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""

while True:

    now = datetime.datetime.now()

    if now >= buy_time_object:
        try:
            # 点击结算按钮
            if driver.find_element_by_id("J_Go"):
                driver.find_element_by_id("J_Go").click()
                print("已经点击结算按钮...")
                while True:
                    try:
                        if "提交次数" < '10':
                            driver.find_element_by_link_text('提交订单').click()
                            print("已经点击提交订单按钮")
                            submit_succ = True
                            break
                        else:
                            print("提交订单失败...")
                    except Exception as ee:
                        print("没发现提交订单按钮，可能页面还没加载出来，重试...")
                        time.sleep(0.1)
        except Exception as e:
            print(e)
            print("不好，挂了，提交订单失败了...")

    time.sleep(0.1)
