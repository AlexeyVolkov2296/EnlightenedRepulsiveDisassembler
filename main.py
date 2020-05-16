documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }
def people (document, ):
    num = input('Введите код документа ')
    code_user_name = ''
    for doc in documents:
        if doc['number'] == num:
            code_user_name += doc['name']
            print(f'Имя сотрудника {code_user_name}')
            break
    else:
        print('Такого чкловека нет в базе')
def shelf (rack):
    num_racks = input('Введите номер документа ')
    my_reks = ''
    for keys, racks in rack.items():
        if num_racks in racks:
            my_reks += keys
            print(f'Номер стелажа {my_reks}')
            break
    else:
        print('Такого сотрудника нету')
def employee_data (employee_list, ):
    num = input('Введите имя сотрудника ')
    full_employee_data = ()
    for employee_dict in employee_list:
        if num in employee_dict['name']:
            full_employee_data += employee_dict['type'], employee_dict['number'], employee_dict['name'], 
            data_about_employee = str(full_employee_data)
            print(f'Данные сотрудника {data_about_employee}')

def add_employee(add_documents, add_shelf):
    document =  input('Введите тип документа: ')
    document_number = input('Введите номер документа: ')
    employee_name = input('Введите имя держателя документа: ')
    new_employee = {"type": '' , "number": '' , 'name':''}
    new_employee['type'] += document
    new_employee['number'] += document_number
    new_employee['name'] += employee_name
    documents.append(new_employee)
    add_in_shelf = input('Введите номер полки на которую вы хотите добавить документы: ')
    if add_in_shelf not in directories.keys():
        directories[add_in_shelf] = []
        directories[add_in_shelf].append(document_number)
        print(f'Сотрудник {employee_name} добавлен в базу данных')
    else:
        directories[add_in_shelf].append(document_number)
        print(f'Сотрудник {employee_name} добавлен в базу данных')

def show_names():
  """Проверка на KeyError"""
  for document in documents:
    try:
      print(f"{document.get('name')}")
    except KeyError:
      print(f"no name")

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p' :
            people(documents)
        elif user_input == 's':
            shelf(directories)
        elif user_input == 'l':
            employee_data(documents)
        elif user_input == 'a':
            add_employee(documents, directories)
        elif user_input == 'e':
            break
main()