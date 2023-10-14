import requests

if __name__ == '__main__':
    # Отправляем запрос на сервер с набором данных
    r = requests.post(
        'http://localhost:5000/api/v1/predict',
        json={
            "bath": 3,
            "sqft": 2000,
            "beds": 3,
            "heating": 1,
            "cooling": 0,
            "parking": 0,
            "age": 99,
            "sch_rat_dist": 7,
            "sch_number": 3,
            "status_Active": 1,
            "status_Other": 0,
            "status_New": 0,
            "status_Pending": 0,
            "status_Foreclosure": 0,
            "propertyType_Single_family": 0,
            "propertyType_Townhouse": 0,
            "propertyType_Condo": 1,
            "propertyType_Multifamily": 0,
            "propertyType_Land": 0,
            "stories_Low_Rise": 0,
            "stories_Mid_Rise": 0,
            "stories_0_Stories": 0,
            "stories_High_Rise": 1,
            "state_0": 0,
            "state_1": 0,
            "state_2": 1,
            "state_3": 1,
            "state_4": 0,
            "state_5": 1
        }
    )
    
    print('Статус сервера:', r.status_code)
    
    if r.status_code == 200:
        print('Ответ сервера - предсказание:', r.json()['prediction'])
    else:
        print('Ответ сервера:', r.text)