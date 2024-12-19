from setuptools import setup, find_packages

setup(
    name="datalib",
    version="0.1.0",
    description="A Python library for data manipulation, statistics, and visualization",
    author="Ibrahim Trabelsi",
    author_email="youremail@example.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
