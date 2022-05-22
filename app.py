from flask import Flask, render_template
import functional

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    '''
    Главная страница со всеми кандидатами
    :return:
    '''
    candidates = functional.get_all_candidates()
    return render_template("list.html",
                           candidates=candidates
                           )


@app.route('/candidates/<int:candidate_id>/')
def page_candidate(candidate_id):
    '''
    Поиск кандидата по его pk
    :param candidate_id:
    :return:
    '''
    candidate = functional.search_by_id(candidate_id)
    if candidate is None:
        return 'Нет такого кандидата'
    return render_template("card.html",
                           candidate=candidate
                           )


@app.route('/search/<candidate_name>/')
def page_search_by_name(candidate_name):
    '''
    Поиск кандидата по его имени
    :param candidate_name:
    :return:
    '''
    candidates = functional.search_by_name(candidate_name)
    number_of_candidates = len(candidates)
    return render_template("search.html",
                            candidates=candidates,
                            number_of_candidates=number_of_candidates
                           )

@app.route('/skill/<name_of_skill>/')
def page_skill(name_of_skill):
    '''
    Поиск по навыкам среди кандидатов
    :param name_of_skill:
    :return:
    '''
    candidates = functional.search_by_skill(name_of_skill)
    number_of_candidates = len(candidates)
    return render_template("skill.html",
                           candidates=candidates,
                           name_of_skill=name_of_skill,
                           number_of_candidates=number_of_candidates
                           )

app.run(debug=True)

