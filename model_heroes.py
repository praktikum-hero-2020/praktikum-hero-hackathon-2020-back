import pickle
model = pickle.load(open('heroes.sav', 'rb'))
loaded_info = [0,1,1,1,0,0,1000,2]
result = model.predict_proba(loaded_info)
print('Вероятность того, что питомца заберут:' , round(result[1], 3) * 100, "%")