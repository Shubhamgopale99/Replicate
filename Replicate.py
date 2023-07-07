import replicate
from dotenv import load_dotenv
load_dotenv()
output = replicate.run(
    "sczhou/codeformer:7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56",
    input={"image": open("C:\\Users\\User\\Downloads\\IMG20221016115634_clipdrop-cleanup.jpg","rb")}
)
print(output)