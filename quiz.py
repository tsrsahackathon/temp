import requests
from os import path

api_key = "5457D9C0W8HO2JDZW2QCRVMNBBWYTMKAR00IGWYB88VQ74SWG0TYQHJQRJZLO7FT"
endpoint = "https://jamsapi.hackclub.dev/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

with open('PUNC_transcript.txt', 'r') as fb:
    texts = fb.read()


messages = []

user_question = "can you create a quiz based on this text? it should have 10 mcq questions? give the response in this format: {\"multiple_choice\": \"[ { \"question\": \"question here\", \"answers\": [ {\"option\": \"option 1\", \"correct\": true/false}, {\"option\": \"option 2\", \"correct\": true/false}, {\"option\": \"option 3\", \"correct\": true/false}, {\"option\": \"option 4\", \"correct\": true/false} ] }, other questions } " + texts

messages.append({"role": "user", "content": user_question})
data = {
    "model": "gpt-3.5-turbo",
    "messages": messages
}
response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    assistant_answer = result["choices"][0]["message"]["content"]
    print(assistant_answer)
    messages.append({"role": "assistant", "content": assistant_answer})
else:
    print(f"Request failed: {response.reason}")
    
fp = open("quiz.txt", "w")
fp.write(assistant_answer)
fp.close()