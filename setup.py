from distutils.core import setup

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='stwits',
    version='0.0.1',
    description='Python client for www.stocktwits.com API',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=['stwits'],
    author='Mark Yosef Joseph',
    author_email='markio@post.bgu.ac.il',
    keywords=['Stock', 'Stocks', 'Twit', 'Twits', 'Tweet', 'Tweets', 'Stocktwits',
              'Stocktwits.com', 'www.Stocktwits.com', 'finance', 'Investing', 'Trading', 
              'Bonds', 'Equities', 'Funds', 'Securities', 'Commodities', 'Crypto'],
    install_requires = ['requests', 'datetime', 'json'],
    url='https://github.com/mark1yo/stwits',
    download_url='https://pypi.org/project/stwits/'
)


if __name__ == '__main__':
    setup(**setup_args)

