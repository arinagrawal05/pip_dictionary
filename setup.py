from setuptools import setup, find_packages

setup(
    name="dictionary",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # "pyperclip",
        # "difflib",
        # "tkinter"
        
    ],
   include_package_data=True,  # This line includes non-code files
    package_data={
        '': ['data.json'],  # Include data.json
    },    entry_points={
        'console_scripts': [
            'dictionary=main:main',  # Assuming you have a main function in main.py
        ],
    },
    description="A speaking dictionary application with text-to-speech functionality.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['dictionary', 'dictionary interface', 'dictionary gui','word search'],

    author="Arin Agrawal",
    author_email="arindeveloper05@gmail.com",
    url="https://github.com/arinagrawal05/pip_dictionary",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   
    ],
    python_requires='>=3.6',  

)
