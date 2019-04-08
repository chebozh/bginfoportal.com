from flask import render_template, request, Blueprint

from BGInfoPortal.models import Article

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template('index.html', title='Начало')


@main.route('/bulgaria')
def bulgaria():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='bulgaria').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                         per_page=15)
    return render_template('bulgaria.html', articles=articles)


@main.route('/world')
def world():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='world').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                      per_page=15)
    return render_template('world.html', articles=articles)


@main.route('/technology')
def technology():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='tech').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                     per_page=15)
    return render_template('technology.html', articles=articles)


@main.route('/economics')
def economics():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='business').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                         per_page=15)
    return render_template('economics.html', articles=articles)


@main.route('/sport')
def sport():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='sport').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                      per_page=10)
    return render_template('sport.html', articles=articles)


@main.route('/interesting')
def interesting():
    page = request.args.get('page', 1, type=int)
    articles = Article.query.filter_by(category='other').order_by(Article.date_added.desc()).paginate(page=page,
                                                                                                      per_page=15)
    return render_template('interesting.html', articles=articles)
