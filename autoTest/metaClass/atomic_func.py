from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
import os
import yaml
import copy
from autoTest.metaClass.logging import Logger
from datetime import datetime


class WebDriver:
    @classmethod
    def getSunName(self):
        sunName = self.__name__
        return sunName

    def __init__(self, filePath):
        self.filePath = filePath
        loggerName = self.getSunName() + '_' + datetime.now().strftime('%m%d_%H%M%S') + '.log'
        loggerName = os.path.join(self.filePath, loggerName)
        self.log = Logger(loggerName, level='debug').logger
        chromeOptions = webdriver.ChromeOptions()
        # 代理
        # chromeOptions.add_argument("--proxy-server=socks5://127.0.0.1:1021")
        chromeOptions.add_argument("--window-size=1920,1080")
        seDriver = webdriver.Chrome(options=chromeOptions, service_log_path='log.log')
        self.seDriver = seDriver
        self.log.info('配置chrome浏览器，启动....')

    def loadYml(self):
        pyFile = self.getSunName()
        stepsYmlFile = os.path.join(self.filePath, pyFile + '.steps.yml')
        assert os.path.exists(stepsYmlFile), f'{stepsYmlFile}文件不存在'
        ymlFile = os.path.join(self.filePath, pyFile + '.yml')

        assert os.path.exists(ymlFile), f'{ymlFile}文件不存在'

        fstepsRead = open(stepsYmlFile, 'r', encoding='utf-8')
        fymlRead = open(ymlFile, 'r', encoding='utf-8')
        fstepsReadcont = fstepsRead.read()
        fymlReadcont = fymlRead.read()
        # steps 文件
        self.ymlFileDict = yaml.load(fstepsReadcont, Loader=yaml.FullLoader)
        # yml文件 内容yml
        self.expandeDict = yaml.load(fymlReadcont, Loader=yaml.FullLoader)
        # 翻译过之后的yml
        self.execStepsYml = {}
        self.gloableGroups = []

        # 文件读写 ，最后要关闭
        fstepsRead.close()
        fymlRead.close()

    def start(self):
        self.loadYml()
        for key, value in self.ymlFileDict.items():
            if 'meta' == key:
                assert value.get('url'), 'URL 路径没有,请填写完在测试'
                for keyGroup, valueGroup in value.items():
                    if keyGroup == 'url':
                        self.log.info(f"打开url连接：{valueGroup}")
                        self.getUrl(valueGroup)

                    if keyGroup == 'groups':
                        if valueGroup:
                            for lineKey in valueGroup:
                                if 'ref' in lineKey.keys():
                                    self.gloableGroups = self.gloableGroups + self.expandeDict[lineKey['ref']]
                        else:
                            raise Exception("groups中没有东西,请填写完在测..")
        ymlWriteFile = os.path.join(self.filePath,  self.getSunName() + '_Run.steps.yml')
        # 这是给人看的，程序没用到
        self.writeDictToYml(ymlWriteFile, self.gloableGroups)
        # 开始运行
        self.RunTest(self.gloableGroups)

    def RunTest(self, listSteps):
        for line in listSteps:
            if 'cmd' in line.keys():
                timeout = line['timeout'] if line.get('timeout') else 30
                cnt = line['cnt'] if line.get('cnt') else 5
                value = line['value'] if line.get('value') else ''
                location = line['location'] if line.get('location') else ''
                if "click" == line['cmd']:
                    self.click(location=location, timeout=timeout, delayTime=1, cnt=cnt)
                if "setValue" == line['cmd']:
                    self.setValue(location=location, value=value, timeout=timeout, cnt=cnt)
                if 'getText' == line['cmd']:
                    self.getText(location, timeout=timeout, cnt=5)
                if 'execApi' == line['cmd']:
                    funcName = line['location']
                    newDic = {k: v for k, v in line.items() if 'cmd' != k and 'location' != k and 'desc' != k}
                    self.call_children(funcName, newDic)

    def call_children(self, funcName, newDic):
        child_method = getattr(self, funcName)  # 获取子类的out()方法
        child_method(**newDic)  # 执行子类的out()方法

    def getText(self, location, timeout=30, cnt=5):
        self.log.info(f"正在尝试获取文字:{location}")
        count = copy.deepcopy(cnt)
        while cnt > 0:
            try:
                self.ensureEleVisble(location, timeout)
                _ele = self.seDriver.find_element_by_xpath(location)
                _text = _ele.text
            except StaleElementReferenceException:
                self.log.error(f"第{count - cnt + 1}次尝试得到{location}的值失败")
                time.sleep(3)
                cnt -= 1
            except Exception as e:
                raise Exception(f"程序发生异常,请检查是否正确使用xpath,报错信息为{e}")
            else:
                self.log.debug(f"获得位置{location} 的值为：{_text}")
                return _text
        assert cnt > 0

    def writeDictToYml(self, yamlpath, desired_caps):
        self.log.info(f"执行步骤写入{yamlpath}文件,您可以查看它的执行过程")
        yaml.dump(desired_caps,
                  open(yamlpath, 'w'),
                  allow_unicode=True,
                  default_flow_style=False)

    def ensureElePresent(self, location, timeout=30):
        assert location, '地址不能为空'
        _ele = WebDriverWait(self.seDriver, timeout).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, location)))
        return _ele

    def ensureEleVisble(self, location, timeout=30):
        assert location, '地址不能为空'
        _ele = WebDriverWait(self.seDriver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, location)))
        return _ele

    def rightClick(self, location, timeout):
        """
            右键点击操作
        :return:
        """
        _ele = self.ensureElePresent(location=location, timeout=timeout)
        _action = ActionChains(self.seDriver)
        _action.context_click(_ele)
        _action.perform()

    def setValue(self, location='', value='', timeout=30, cnt=0):
        while cnt > 0:
            try:
                self.ensureElePresent(location, timeout)
                _ele = self.seDriver.find_element_by_xpath(location)
                _ele.send_keys(Keys.CONTROL, 'a')
                _ele.send_keys(Keys.DELETE)

                value = str(value)
                [_ele.send_keys(line) for line in value]
                _getValue = _ele.get_attribute('value')
                assert value == _getValue, f"没有正确输入值{location}"
            except Exception as _:
                self.log.error(f"设置的值有问题{location}")
                time.sleep(3)
                cnt -= 1
            else:
                break
        assert cnt > 0, f'多次尝试setValue 失败{location}'

    def click(self, location, timeout=30, delayTime=1, cnt=5):
        """
            点击操作
        :param location:
        :param value:
        :param timeout:
        :param delayTime:
        :return:
        """
        if delayTime:
            time.sleep(delayTime)

        while cnt > 0:
            try:
                _ele = WebDriverWait(self.seDriver, timeout).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, location))
                )
                _ele.click()
            except:
                time.sleep(delayTime)
                cnt -= 1
            else:
                break
        assert cnt > 0, '尝试多次仍然没有找到这个位置'

    def executeJavaScript(self, script, *args):
        self.seDriver.execute_script(script, *args)

    def screenShot(self, filename):
        self.seDriver.save_screenshot(filename)

    def getUrl(self, url):
        self.seDriver.get(url)


def timeMS():
    _str = str(int((time.time() * 1000000)))
    return _str[4:]
