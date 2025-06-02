from setuptools import setup, find_packages

setup(
    name="multilang-python",
    version="0.1.0",
    packages=["multilang_python"],
    package_dir={"multilang_python": "src"},
    entry_points={
        "console_scripts": [
            "multilang-python=multilang_python.interfaces.cli:main"
        ]
    },
    author="Abdou-Raouf ATARMLA",
    author_email="achilleatarmla@gmail.com",
    description="A transpileur for Python in native languages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fless-lab/multilang-python",
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)