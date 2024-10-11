import json
import time
from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




@given("install and launch MyObservatory app")
def install_launch_app(context):
	context.driver = webdriver.Remote(context.appium_url, desired_capabilities=context.appium_settings)


@given("allow permissions")
def allow_p(context):
	driver = context.driver
	agree = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "hko.MyObservatory_v1_0:id/btn_agree")))
	agree.click()
	agree.click()
	allow1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1")))
	allow1.click()
	allow2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID,
							  "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
	allow2.click()
	allow3 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")))
	allow3.click()

@when("close AD screens")
def close_ad(context):
	driver = context.driver

	next_p = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "hko.MyObservatory_v1_0:id/exit_btn")))
	next_p.click()
	next_p.click()
	next_p.click()



@when("click left side menu")
def click_menu(context):
	driver = context.driver

	menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Navigate up")))
	menu.click()


@when("click 9-day forecast item")
def click_forecast_item(context):
	driver = context.driver
	time.sleep(2)
	forecast_item = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH,
							  "//android.widget.TextView[@resource-id=\"hko.MyObservatory_v1_0:id/title\" and @text=\"Forecast & Warning Services\"]")))
	forecast_item.click()
	time.sleep(1)
	sub_item = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH,
							  "//android.widget.TextView[@resource-id=\"hko.MyObservatory_v1_0:id/title\" and @text=\"9-Day Forecast\"]")))
	sub_item.click()

@then("navigate 9-day forecast screen successfully")
def navigate_forecast_page(context):

	driver = context.driver
	top_title = WebDriverWait(driver, 30).until(
		EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Weather Forecast\"]")))

	second_title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text=\"9-Day Forecast\"]")))
	introduction = WebDriverWait(driver, 30).until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit\"]")))

	data = {"introduction": introduction.text}
	with open("features/result.json", "w", encoding='utf-8') as file:
		json.dump(data, file)

	assert introduction.text != "", f"Failed to get introduction, the element is {introduction}, introduction : {introduction.text}"
	assert top_title.text == "Weather Forecast", "Top Title is not 'Weather Forecast'"
	assert second_title.text == "9-Day Forecast", "The second title is not '9-Day Forecast'"
