import requests
import json
import argparse
import urllib3
from pyfiglet import Figlet

banner = Figlet(font="slant")
print(banner.renderText("Swagger") + "\nSwagger-api-docs接口提取\n")

parser = argparse.ArgumentParser(description='')
parser.add_argument('-u', '--url', default='')
arg = parser.parse_args()
urllib3.disable_warnings()  # 屏蔽证书警告


def swagger(url):
    # Swagger API文档的URL
    swagger_url = url

    # 发送HTTP请求获取Swagger的API文档
    response = requests.get(swagger_url)

    # 解析文档中的接口地址
    if response.status_code == 200:
        api_docs = json.loads(response.text)
        paths = api_docs.get("paths", {})
        for path, methods in paths.items():
            for method, info in methods.items():
                # print(f"{path}")
                if f"{method}" == "post":
                    # print("post:\n")
                    # print(f"{method}  {path}")
                    user = open("swagger_post.txt", 'a', encoding='UTF-8')
                    user.write(f"{path}")
                    user.write('\n')
                    user.close()
                else:
                    user = open("swagger_get.txt", 'a', encoding='UTF-8')
                    user.write(f"{path}")
                    user.write('\n')
                    user.close()
        print("[*]--提取完成!!!")

    else:
        print(f"Failed to retrieve API docs: {response.status_code}")


if __name__ == "__main__":
    if arg.url != '':
        swagger(arg.url)
