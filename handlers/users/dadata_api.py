from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import db, dp
from dadata import Dadata


def dadata_check(inn):
    token = "20473d0a0f63fdc5c6921b0d9b54ae2ca0745429"
    dadata = Dadata(token)
    data = dadata.find_by_id("party", inn)

    if data != []:
        return True
    else:
        return False


def dadata_start(id, inn):
    token = "20473d0a0f63fdc5c6921b0d9b54ae2ca0745429"
    dadata = Dadata(token)
    data = dadata.find_by_id("party", inn)

    company_info = data[0]

    dict_parametr = {'cont_org': company_info['value'],
                     'cont_ogrn': company_info['data']['ogrn'],
                     'cont_adress': company_info['data']['address']['unrestricted_value'],
                     'cont_fio': company_info['data']['management']['name'],
                     'cont_headstatus': company_info['data']['management']['post'],
                     'cont_inn': inn

                     }

    db.update_cont_user(cont_id=id, dict_oper=dict_parametr)

    sql = "SELECT * FROM lst_oper WHERE type = %s;"
    result = db.execute(sql, parameters=('cont_user',), fetchall=True)
    result = list(result)

    lst_oper = ['cont_org', 'cont_ogrn', 'cont_adress',
                'cont_fio', 'cont_headstatus', 'cont_inn']

    element_to_move = None
    for oper in lst_oper:
        for x in result:
            if oper in x:
                element_to_move = x

        index_of_element = result.index(element_to_move)

        result.pop(index_of_element)

    return result
