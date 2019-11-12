import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
	# take db URL from DATABASE_URL environment variable OR
	# configure database in local dir named app.db
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://quizmenow:DataRockstar@localhost:3306/quizmenow'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'