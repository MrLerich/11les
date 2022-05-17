from flask import Flask
import functional

app = Flask(__name__)


@app.route('/')
def all_candidates():
    '''
    Главная страница со всеми кандидатами
    :return:
    '''
    candidates = functional.get_all_candidates()
    code_of_html = functional.html_view_candidates(candidates)

    return code_of_html


@app.route('/skills/<skill>')
def search_by_skill(skill):
    '''
    Поиск по навыкам среди кандидатов
    :param skill:
    :return:
    '''
    candidates = functional.search_by_skill(skill)
    code_of_html = functional.html_view_candidates(candidates)

    return code_of_html


@app.route('/candidates/<int:pk>')
def search_by_id(pk):
    '''
    Поиск кандидата по его pk
    :param pk:
    :return:
    '''
    candidate = functional.search_by_id(pk)
    code_of_html = functional.html_view_selected_candidate(candidate)

    return code_of_html

@app.route('/candidates/<candidate_name>')
def search_by_name(candidate_name):
    '''
    Поиск кандидата по его имени
    :param name:
    :return:
    '''
    candidate = functional.search_by_name(candidate_name)
    code_of_html = functional.html_view_selected_candidate(candidate)

    return code_of_html

app.run(debug=True)

