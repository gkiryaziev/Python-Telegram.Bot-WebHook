from setuptools import setup, find_packages

from telegram_bot import __version__, __license__

setup(
    name='telegram_bot',
    author='gkiryaziev',
    author_email='@',
    version=__version__,
    url='url',
    license=__license__,
    python_requires='>=3',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    description="Python-Telegram.Bot-WebHook.",
    install_requires=[
        'Flask==1.0',
        'requests==2.18.4',
    ],
    entry_points={
        'console_scripts':
            ['telegram_bot = telegram_bot.core:main']
    },
    include_package_data=True,
    zip_safe=False
)
