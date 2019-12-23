import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV', 'develop')

app = create_app(env)
# app.config.from_pyfile('settings.py')
# app.config.from_object(settings)  # 加载配置文件

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
