from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TaskFeasibilityAnalyzer',
    version='0.0.4',
    description='A Python package to determine the feasibility of coding tasks using GPT-3.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    url='https://github.com/chigwell/TaskFeasibilityAnalyzer',
    packages=find_packages(),
    install_requires=[
        'openai',
        'projectstructor',
        'gptintegration',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
