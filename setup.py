from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='stwits',
    version='1.0.0',
    description='Python client for www.stocktwits.com API',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Mark Yosef Joseph',
    author_email='markio@post.bgu.ac.il',
    keywords=['Stock', 'Stocks', 'Twit', 'Twits', 'Tweet', 'Tweets', 'Stocktwits',
              'Stocktwits.com', 'www.Stocktwits.com', 'finance', 'Investing', 'Trading', 
              'Bonds', 'Equities', 'Funds', 'Securities', 'Commodities', 'Crypto'],
    url='https://github.com/mark1yo/stwits',
    download_url='https://pypi.org/project/stwits/'
)

install_requires = [
    'requests',
    'datetime',
    'json'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
