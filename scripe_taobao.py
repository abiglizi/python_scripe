from selenium import webdriver
import datetime
import time


def login():
    '''
    browser.get('https://login.taobao.com/member/login.jhtml')
    cookies = [{}]

    for item in cookies:
        browser.add_cookie(item)
    browser.get('https://www.taobao.com')

    #browser.get("https://cart.taobao.com/cart.htm")

    time.sleep(3)
    '''
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(5)

    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"请尽快扫码登录")
        time.sleep(15)

    #'''


def picking_buy(method,times):
    # 打开购物车列表页面
    browser.get("https://cart.taobao.com/cart.htm")

    time.sleep(3)

    # 是否全选购物车
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll2"):
                    browser.find_element_by_id("J_SelectAll2").click()
                    break
            except:
                print(f"找不到购买按钮")
    else:
        print(f"请手动勾选需要购买的商品")
    while True:
        if browser.find_element_by_id("J_SelectedItemsCount").text > '0':
            print("购物车不为空，继续下一步")
            break
        time.sleep(0.3)
        print(browser.find_element_by_id("J_SelectedItemsCount").text)

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # python中字符串的大小比较，是按照字符顺序，从前往后依次比较字符的ASCII数值
        # 对比时间，时间到的话就点击结算
        #time.sleep(0.5)  # 延时，以修正时间
        if now >= times:
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        while True:
                            try:
                                if browser.find_element_by_link_text('提交订单'):
                                    browser.find_element_by_link_text('提交订单').click()
                                    print(f"抢购成功，请尽快付款")
                                    break
                            except:
                                print(f"（2）没找到按钮，再次尝试提交订单")
                                time.sleep(0.05)
                    else:
                        print("(1)出现错误，结算失败")
                except:
                    print("（0）出现错误，失败")


            '''
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    print("找不到按钮")
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print(f"抢购成功，请尽快付款")
                        break
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.1)
            '''

if __name__ == "__main__":

    # 请指定勾选购物车商品的方式
    # 0代表，自动勾选购物车内的全部商品。注意：若购物车中存在失效商品时无法进行全选，请勿使用此项
    # 1代表，手动勾选购物车内的商品
    method = 1
    # 请指定抢购时间，时间格式："2019-06-01 10:08:00.000"
    times = "2019-11-11 00:00:00.00000"
    # 自动打开Chrome浏览器
    browser = webdriver.Chrome()
    # 设置浏览器最大化显示
    browser.maximize_window()
    # 登录淘宝
    login()
    # 勾选准备结算的商品,等待抢购时间，定时秒杀
    picking_buy(method,times)



