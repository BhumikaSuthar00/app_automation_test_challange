from appium import webdriver
import os


class Main:
    def __init__(self):
        # We can read config from YAML or Config JSON from CI/CD
        apk_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apk/app-debug.apk'))
        #Create config files based on the device type and os
        self.androidEmulaterConfig = {
            "platformName": "Android",
            "platformVersion": "11.0",
            "deviceName": "pixel_xl",
            "app": apk_location,
            "appPackage": "codepath.apps.demointroandroid",
            "appActivity": "codepath.apps.demointroandroid.DemoSelector",
            "automationName": "UiAutomator2"
        }
        try:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.androidEmulaterConfig)
            # Wait for till its find xpath. XPATH is very time consuming and may take some time. Hence wait for more time
            self.driver.implicitly_wait(2)
            chapter1 = self.driver.find_elements_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[1]')[
                0]
            # Test_Case_1
            self.assertValueTextValue('Test_Case_1', chapter1, 'Chapter 1: App Fundamentals')
            chapter1.click()
            # Find underlyaing list item
            self.driver.implicitly_wait(2)
            basicText = self.driver.find_elements_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[2]')[
                0]
            # Test_Case_2
            self.assertValueTextValue('Test_Case_2', basicText, 'Basic TextView')
            basicText.click()
            # Test_Case_3
            self.driver.implicitly_wait(2)
            secondTextView = self.driver.find_elements_by_xpath('hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView')[0]
            self.assertValueTextValue('Test_Case_3', secondTextView, 'Second TextView for Chapter 1')
            # Goback
            self.androidGoBack()

            # Test_Case_4
            self.driver.implicitly_wait(2)
            userInterface = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[3]')[0]
            self.assertValueTextValue('Test_case_4', userInterface, 'Chapter 2: User Interface')
            userInterface.click()
            # Test_Case_5 Chapter 4 Button
            self.driver.implicitly_wait(2)
            chapter4 = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[6]')[0]
            self.assertValueTextValue('Test_case_5', chapter4, 'Chapter 4: User Interactions')
            chapter4.click()
            # Test Case_6 basic click handler
            self.driver.implicitly_wait(2)
            basicClickHander = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[11]')[0]
            self.assertValueTextValue('Test_case_6', basicClickHander, 'Chapter 7: Advanced Views')
            basicClickHander.click()
            # Test_case_7 Button
            self.driver.implicitly_wait(2)
            xmlButton = self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ExpandableListView/android.widget.TextView[12]')[0]
            self.assertValueTextValue('Test_case_7', xmlButton, 'Toast Inputs')
            xmlButton.click()

        except Exception as ex:
            print(ex)
            print('Driver connection failed. Please check your configuration')

    def assertValueTextValue(self, textCaseId, el, value):
        try:
            assert el.text == value
            print(textCaseId + ' Passed!')
            return
        except:
            print(textCaseId + ' Failed!')
            return

    def androidGoBack(self):
        self.driver.back()
        print('Going Back')

Object = Main()