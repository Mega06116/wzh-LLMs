from transformers import AutoTokenizer, AutoModel
MODEL_PATH = ('D:/wzh/models')
TOKENIZER_PATH=MODEL_PATH
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).cuda()
model=model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)