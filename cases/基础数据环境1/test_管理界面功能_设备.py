import time

import pytest
from selenium.webdriver.common.by import By

from cfg import *
from lib.webUI_smp import smpUI

@pytest.fixture
def delAddedDevice() :
    yield

    print('*** 删除第一个设备 ***')
    smpUI.del_first_item()

def test_SMP_device_001(createBasicEnv1, delAddedDevice):
    smpUI.wd.get(SMP_URL_DEVICE)

    time.sleep(1)

    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR,'.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    # 电瓶车充电站
    info = smpUI.add_device('电瓶车充电站', 'bokpower-charger-g22-220v300w',
                             '全国-电瓶车充电费率1', 'aaaaaaaa', '杭州秀月家园7幢1单元-充电站')

    devSharedScrete = info.pop(3)
    assert info == ['电瓶车充电站', 'bokpower-charger-g22-220v300w', 'aaaaaaaa',
                    '全国-电瓶车充电费率1', '杭州秀月家园7幢1单元-充电站']

    assert len(devSharedScrete) == 32