import yaml


data = {"a":"123","bb": "我忘记看见了考虑"}
with open("aa.yaml","w", encoding="utf-8") as f:
    yaml.dump(data,f,allow_unicode=True)
    # yaml.dump(data,f,allow_unicode=True)