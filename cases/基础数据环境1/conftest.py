import pytest,time
from lib.webUI_smp import smpUI
from selenium.webdriver.common.by import By
from cfg import *

# 设备自动化的前提是有一些 设备型号和设备规则，

# 很多人以为应该指定执行次序，放在  设备型号和设备规则用例后面执行

# 不能这样！！！！！！！！！！！

# 本模块的共享数据 SMP_UI 实例

@pytest.fixture(scope='package',autouse=True)
def createBasicEnv1():
    print(f'\n==== setup： baseEnv1 ')
    smpUI.login('byhy','sdfsdf' )

    
    print('SMP 添加设备型号')
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)

    # 点击添加按钮
    smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span').click()

    
    # 电瓶车充电站
    smpUI.add_device_model("电瓶车充电站",
                          'bokpower-charger-g22-220v300w',
                          '杭州bok 2022款300瓦 电瓶车充电站')
    
    # 洗车站
    smpUI.add_device_model("洗车站",
                          'njcw-carwasher-g22-2s',
                          '南京e生活2022款洗车机 2个洗车位')
    
    # 存储柜
    smpUI.add_device_model("存储柜",
                          'elife-canbinlocker-g22-10-20-40',
                          '南京e生活2022款存储柜-10大20中40小')

    time.sleep(1)
    print('SMP 添加业务规则')
    smpUI.wd.get(SMP_URL_SERVICE_RULE)

    # 点击添加按钮
    smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span').click()
    
    # 预付费-下发业务量
    smpUI.add_svc_rule("全国-电瓶车充电费率1",
                      "预付费-下发业务量",
                      "0.1",
                      "2",
                      ['千瓦时', '1.0'],
                      "")
    
    # 预付费-下发费用
    smpUI.add_svc_rule("深圳-洗车机费率1",
                      "预付费-下发费用",
                      "2",
                      "10")
    
    # 后付费-上报业务量
    smpUI.add_svc_rule("南京-存储柜费率1",
                      "后付费-上报业务量",
                      "",
                      "",
                      [['100L', '小时', '2'], ['50L', '小时', '1'], ['10L', '小时', '0.5']],
                      "", )

    yield


    print('删除业务规则')
    smpUI.wd.get(SMP_URL_SERVICE_RULE)
    for i in range(3):
        time.sleep(1)
        smpUI.del_first_item()

    print('删除设备型号')
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)
    for i in range(3):
        time.sleep(1)
        smpUI.del_first_item()