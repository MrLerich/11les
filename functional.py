import json

path = 'candidates.json'

def get_data():
    '''
    Возвращает даннные про кандидатов
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
    candidates = get_data()
    return candidates


def search_by_id(candidate_id):
    '''
    Получает кандидата по его id
    :param candidate_id:
    :return:
    '''
    candidates = get_data()
    for candidate in candidates:
        if candidate.get('id') == candidate_id:
            return candidate


def search_by_name(candidate_name):
    '''
    Получает кандидата по его имени
    :param candidate_name:
    :return:
    '''
    candidates = get_data()
    founded_candidates = []
    for candidate in candidates:
        if candidate_name.lower() in candidate.get('name').lower():
            founded_candidates.append(candidate)
    return founded_candidates


def search_by_skill(name_of_skill):
    '''
    Ищем кандидата по наличию скила
    :param name_skill:
    :return:
    '''
    candidates = get_data()
    candidate_with_skill = []
    name_of_skill_lower = name_of_skill.lower()

    for candidate in candidates:
        skills = candidate.get('skills')
        lst_of_skills = skills.lower().strip().split(', ')
        if name_of_skill_lower in lst_of_skills:
            candidate_with_skill.append(candidate)
            continue
    return candidate_with_skill





