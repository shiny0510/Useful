from models.ImageGener import StyleGAN
from models.TTS import tacotron


model = StyleGAN()
mode2 = tacotron()

for epoch in epochs:
    for idx, data in enumerate(dataloader):


# 학습 완료되면 model.pt가 저장.