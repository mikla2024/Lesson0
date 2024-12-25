note1 = {
    'username': 'crazy_joe',
    'content': 'shopping list', 
    'status': 'in_progress',
    'created_date': '25.12.2024',
    'issue_date': '25.01.2025',
    'titles': ['milk', 'eggs', 'bread']
    }

status_dict = {
    "1" : "Выполнено", "2" : "Отложено", "3" : "В процессе"
    }

print('Данные заметки:\n')
for k,v in note1.items():
    print (f'{k}: {v}')

print('\n')

for k,v in status_dict.items():
    print (f'{k}: {v}')


while True:
    status = input(
    "\nВыберите статус заметки из предложенных выше нажав"
    "соотвествующию цифру: "
    )     
    print(f'\nВаш выбор: {status}')
    if status in ['1','2','3']:
        note1['status'] = status_dict.get(status)
        print('\nСтатус заметки обновлен:\n')
        for k,v in note1.items():
            print (f'{k}: {v}')
        break
    else:
        print('Некорректный выбор. Попробуйте еще раз')		
        continue
