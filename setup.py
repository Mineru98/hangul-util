from setuptools import find_packages, setup

setup(
    name="py-hangul-utils",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="iamiks",
    author_email="mineru664500@gmail.com",
    description="한글 유틸 패키지",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mineru98/py-hangul-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
