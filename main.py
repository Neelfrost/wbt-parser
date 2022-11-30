import json

from bs4 import BeautifulSoup

qlist = []
alist = []

with open("input.txt", "r") as txt_file:
    contents = txt_file.read()
    contents = contents.replace("<script>H5PIntegration = ", "").replace(
        ";</script>", ""
    )
    with open("data.json", "w") as json_file:
        json_file.write(contents)

with open("data.json", "r") as file:
    data = json.load(file)

content = data.get("contents")
jsonContent = json.loads(content.get(list(content.keys())[0]).get("jsonContent"))
questions = jsonContent.get("questions")

for item in questions:
    params = item.get("params")

    question = params.get("question", "")
    qlist.append(BeautifulSoup(question, "html5lib").text.strip())

    # Handle true false questions
    if params.get("correct"):
        alist.append("True")
        continue

    # Handle MCQs
    answers = params.get("answers", {})
    for answer in answers:
        if answer.get("correct"):
            alist.append(BeautifulSoup(answer.get("text"), "html5lib").text.strip())
            break

for q, a in zip(qlist, alist):
    print("Q: ", q)
    print("A: ", a)
    print("-" * 78)
