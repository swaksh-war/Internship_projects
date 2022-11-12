import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize





cont = """

=======================================
            Welcome to Villy
=======================================
Note: Type 'quit' to exit bot.
---------------------------------------

"""

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE, map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Villy"
print(cont)
detected_issues = []
# while True:
#     # sentence = "do you use credit cards?"
#     sentence = input("You: ")
#     if sentence == "quit":
#         break

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]
    

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 if tag in ["mental","skin","fracture"]:
#                     detected_issues.append(tag)
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         ex_response = ["Sorry,I am not able to get what you want to say :(","Can you please write it more clearly.","I think I am having an issue understanding you."]
#         er = random.randint(0,2)
#         print(f"{bot_name}: {ex_response[er]} ")
# print(f"Detected Disease from Chat: {detected_issues}")

def get_response(message):
    sentence = tokenize(message)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag in ["mental","skin","fracture"]:
                    detected_issues.append(tag)
                return f"{random.choice(intent['responses'])}"
    else:
        ex_response = ["Sorry,I am not able to get what you want to say :(","Can you please write it more clearly.","I think I am having an issue understanding you."]
        er = random.randint(0,2)
        return f"{ex_response[er]}"
