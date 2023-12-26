import torch

model = torch.load("model.pt")

model.eval()

predict = model(데이터)

print(predict)