import dvc.api
from dvc.api import DVCFileSystem

url = "https://github.com/albino4967/dvc_registry.git"
fs = DVCFileSystem(url, rev="feature/DVC")

print(fs)

text = fs.read_text("result/result.txt", encoding="utf-8")
print(fs.find("/", detail=False, dvc_only=True))
fs.get_file("result/result.txt", 'result.txt')

# data = dvc.api.read(
#     'result/result.txt',
#     repo = 'https://github.com/albino4967/dvc_registry.git',
#     mode = 'rb'
# )
#
# print(data)