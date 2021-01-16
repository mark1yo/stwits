from distutils.core import setup

setup_args = dict(
    name='stwits',
    description='Python client for www.stocktwits.com API',
    version='0.0.1',
    license='MIT',
    author='Mark Yosef Joseph',
    author_email='markio@post.bgu.ac.il',
    packages=['stwits'],
    keywords=['Stock', 'Stocks', 'Twit', 'Twits', 'Tweet', 'Tweets', 'Stocktwits',
              'Stocktwits.com', 'www.Stocktwits.com', 'finance', 'Investing', 'Trading', 
              'Bonds', 'Equities', 'Funds', 'Securities', 'Commodities', 'Crypto'],
    install_requires = ['requests', 'datetime', 'json'],
    url='https://github.com/mark1yo/stwits',
    download_url='https://pypi.org/project/stwits/'
)


if __name__ == '__main__':
    setup(**setup_args)

