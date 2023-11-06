import requests

api_key = "5457D9C0W8HO2JDZW2QCRVMNBBWYTMKAR00IGWYB88VQ74SWG0TYQHJQRJZLO7FT"
endpoint = "https://jamsapi.hackclub.dev/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

fb = open('PUNC_transcript.txt', 'r')
textx = fb.read()
fb.close()


messages = []

user_question = "can you summarize the text" + textx

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

hold = open("summary.txt", "w")
hold.write(assistant_answer)
hold.close()
