import json


def before_all(context):
	context.appium_url = "http://localhost:4723/wd/hub"
	context.appium_settings = {
		"platformName": "Android",
		"platformVersion": "10",
		"deviceName": "JPF4C19228001786",
		"appPackage": "hko.MyObservatory_v1_0",
		"appActivity": "hko.MyObservatory_v1_0.AgreementPage",
		"noReset": "false",
		"appWaitForLaunch": "false",
		"app": "G:\\appDemo\\mobileUI-demo\\hko.MyObservatory_v1_0.apk"
	}
	context.api_baseUrl = "https://pda.weather.gov.hk/"
	context.nineDay_forecast_endpoint = "locspc/android_data/fnd_e.xml"
	context.local_forecast_endpoint = "locspc/android_data/flw_wxicons.xml"
	context.nineDay_forecast_introduction = None

def after_all(context):
	with open("result.json", "a+", encoding="utf-8") as file:
		data = json.load(file)

	if data.get("introduction"):
		data['introduction'] = None
		json.dump(data, file)
