import os
import re
from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = "\n".join([x for x in f.read().split("\n") if not x.startswith('>')])

with open("requirements.txt", encoding="utf-8") as r:
    install_requires = [i.strip() for i in r if not i.startswith('#')]

with open("pynigger/constants.py", "r", encoding="utf-8") as f:
    text = f.read()
    pat = r"['\"]([^'\"]+)['\"]"
    version = re.search("__version__ = "+pat, text).group(1)
    # beta_version = re.search("__beta_version__ = "+pat, text).group(1)
    description = re.search("__description__ = "+pat, text).group(1)


def get_packages():
    return [path.replace("\\", ".").replace("/", ".") for path, _, _ in os.walk("pynigger") if "__" not in path]


setup(
    name='PyNigger',
    packages=get_packages(),
    version=version,
    license='GPLv3+',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GerProgrammer',
    author_email='unknownusernametopick@gmail.com',
    url='https://github.com/unknownusernametopick/PyNigger',
    keywords=['telegram', 'bot', 'pyrogram', 'python', 'telegram-bot'],
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.9",
    dependency_links=['https://github.com/pyrogram/pyrogram/tarball/master'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Natural Language :: English',
        'Topic :: Communications :: Chat',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    project_urls={
        "Support": "https://t.me/NiGGeR_BotsChat",
        "Community": "https://t.me/NiGGeR_Bots",
        "Updates": "https://t.me/pynigger",
        "Documentation": "https://pynigger.codes/",
    },
    entry_points={
        'console_scripts': [
            'pynigger = pynigger.cli:main',
        ],
    },
)
