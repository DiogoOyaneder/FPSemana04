import json
file = input("")
try:
    with open(file, encoding='utf-8') as json_data:
        data = json.load(json_data)
        print(data)
except:
    print ("Ocorreu um erro!")
finally:
     print("Processo concluído!")