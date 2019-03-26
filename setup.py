from setuptools import setup

setup(name='PgEngine',
      version='0.1',
      description='Postgres Python Engine',
      url='',
      author='Prabir Ghosh',
      author_email='mymail.prabir@gmail.com',
      license='MIT',
      packages=['PgEngine'],
      install_requires=["pandas","sqlalchemy"],
      zip_safe=False)