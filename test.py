import pandas as pd

# 데이터 로드
data = pd.read_csv('news_dataset.csv')
texts = data['text'].tolist()
labels = data['label'].tolist()

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 토큰화
tokens = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

from transformers import BertForSequenceClassification
import torch

# BERT 모델 로드
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=5)

# GPU 사용 설정 (선택 사항)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

from torch.utils.data import DataLoader, TensorDataset
from transformers import AdamW

# 데이터셋 준비
dataset = TensorDataset(tokens['input_ids'], tokens['attention_mask'], torch.tensor(labels))
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

# 옵티마이저 설정
optimizer = AdamW(model.parameters(), lr=2e-5)

# 손실 함수
loss_fn = torch.nn.CrossEntropyLoss()

model.train()
for epoch in range(3):  # 에포크 수는 조정 가능
    for batch in dataloader:
        input_ids, attention_mask, labels = [item.to(device) for item in batch]

        # 모델 출력 계산
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        # 역전파 및 옵티마이저 스텝
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

from sklearn.metrics import accuracy_score

model.eval()
predictions, true_labels = [], []

with torch.no_grad():
    for batch in dataloader:
        input_ids, attention_mask, labels = [item.to(device) for item in batch]

        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predictions.append(logits.argmax(dim=1).cpu().numpy())
        true_labels.append(labels.cpu().numpy())

# 정확도 계산
accuracy = accuracy_score(true_labels, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

