import requests

contents = requests.get("https://adventofcode.com/2019/day/1/input", headers={"Cookie": "_ga=GA1.2.932380314.1606769568; "
                                                                                        "_gid=GA1.2.674337088.1606769568; "
                                                                                        "session=53616c7465645f5f3c6aeb045681a7f27a9873ebaeec6c3c141f3110243e04f7a654bd83916d38359a6cc23110eaba4a"})

print(contents.status_code)
print(contents.headers)
print(contents.content)
