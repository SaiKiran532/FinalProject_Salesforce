import requests


def verify_api_response_status(api_url):
    header_value = {"Context-Type": "application/json", "Accept-Encoding": "deflate"}
    response = requests.get(api_url, headers=header_value)
    if response.status_code == 200:
        return print(str(response.status_code)+" is successful HTTP status code")
    else:
        return print(str(response.status_code)+"  is not a successful HTTP status code")


api_url = 'https://api.coincap.io/v2/assets'

verify_api_response_status(api_url)
