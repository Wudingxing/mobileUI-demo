import json
from behave import given, when, then
from datetime import datetime
import requests


@given("9-day forecast related endpoint")
def get_9Day_endpoint(context):
	context.endpoint = context.nineDay_forecast_endpoint

@given("local forecast related endpoint")
def get_local_endpoint(context):
	context.endpoint = context.local_forecast_endpoint

@when('send a request with {param}')
def send_request(context, param):
	base_url = context.api_baseUrl
	req_body = {}
	header = {"authority": "pda.weather.gov.hk",
			  "scheme": "https",
			  "cache-control": "max-age=0",
			  "accept-encoding": "gzip",
			  "user-agent": "okhttp/4.12.0 (Android 10; HUAWEI VCE-AL00) MyObservatory/5.",
			  }
	if param == 'normal':
		pass

	elif param == 'if-modified-since':
		header["if-modified-since"] = "Thu, 10 Oct 2024 16:45:28 GMT"

	elif param == 'fake_endpoint':
		context.endpoint = "abc123"

	elif param == 'fake_body':
		req_body = {"data": 123}

	context.response = requests.get(url=base_url + context.endpoint, headers=header, data=req_body)


@then('response status code is {code}')
def verify_statusCode(context, code):
	status_code = context.response.status_code
	assert status_code == int(code), f"Expected is {code}, but Actual is {status_code}"


@then('verify results are consistent with related content on 9-day forecast page')
def verify_response(context):
	content = context.response.content.decode("utf-8")
	content = json.loads(content)
	with open("features/result.json", 'r', encoding='utf-8') as data_file:
		result = json.load(data_file)
	assert content["general_situation"] == result.get("introduction"), f"The 9-day introduction from API is not matched from UI displaying {result.get('introduction')}"



@then("no any content from response")
def verify_response(context):
	result = context.response.content.decode("utf-8")
	assert result == "", "The response content is not None"


@then("get humidity for the day after tomorrow")
def get_humidity(context):
	min_hd, max_hd = None, None
	forecast_list = json.loads(context.response.content.decode("utf-8")).get("forecast_detail")
	current_date = datetime.now()
	formatted_date = int(current_date.strftime('%Y%m%d'))
	tdat_date = str(formatted_date + 2)
	for day in forecast_list:
		if day['forecast_date'] == tdat_date:
			min_hd = day['min_rh']
			max_hd = day['max_rh']

	print(f"the humidity for the day after tomorrow is {min_hd} - {max_hd}%")
