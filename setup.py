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
    description="A transpileur for Python in native languages",
    license="MIT",
    python_requires=">=3.6",
    include_package_data=True,
)