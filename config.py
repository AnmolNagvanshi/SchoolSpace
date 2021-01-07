import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://anmol:anmol@localhost/school'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    UPLOAD_FOLDER_TC = 'uploads/tc'
    UPLOAD_FOLDER_MIGRATION = 'uploads/migration'
    UPLOAD_FOLDER_PHOTO = 'uploads/photo'
    UPLOAD_FOLDER_SOLUTION = 'uploads/solution'
    UPLOAD_FOLDER_ASSIGNMENT = 'uploads/assignment'
    UPLOAD_FOLDER_TEACHER_DP = 'uploads/teachers/dp'


