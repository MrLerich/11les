import json

PATH = 'candidates.json'

def get_data(path=PATH):
    '''
    Загружает даннные про кандидатов
    :param path:
    :return:
    '''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all_candidates():
    '''
    Список всех кандидатов
    :return:
    '''
    data = get_data()
    return data


def search_by_id(pk):
    '''
    Получает кандидата по его id
    :param pk:
    :return:
    '''
    candidates = get_data()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate


def search_by_name(candidate_name):
    '''
    Получает кандидата по его имени
    :param candidate_name:
    :return:
    '''
    candidates = get_data()
    for candidate in candidates:
        if candidate['name'] == candidate_name:
            return candidate


def search_by_skill(name_of_skill):
    '''
    Ищем кандидата по наличию скила
    :param name_skill:
    :return:
    '''

    candidate_with_skill = []
    name_of_skill_lower = name_of_skill.lower()

    candidates = get_data()
    for candidate in candidates:
        skills = candidate['skills'].lower().strip().split(', ')
        if name_of_skill_lower in skills:
            candidate_with_skill.append(candidate)
            continue

    return candidate_with_skill





def html_view_selected_candidate(candidate):
    '''
    Вид html выбранного кандидата
    :param candidate:
    :return:
    '''
    candidate_selected = ''

    candidate_selected += f"<img src='{candidate['picture']}'>\n"
    candidate_selected += f"{candidate['name']}\n"
    candidate_selected += f"{candidate['skills']}\n"
    candidate_selected += f"{candidate['position']}\n"
    candidate_selected += "\n"

    return '<pre>' + candidate_selected + '</pre>'


def html_view_candidates(candidates):
    '''
    Вид html кандидатов
    :param candidates:
    :return:
    '''
    candidates_lst = ''
    for candidate in candidates:

        candidates_lst += f"{candidate['name']}\n"
        candidates_lst += f"{candidate['skills']}\n"
        candidates_lst += f"{candidate['position']}\n"
        candidates_lst += "\n"

    return '<pre>' + candidates_lst + '</pre>'



