from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="sensevoice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=required,
    author="FunAudioLLM",
    author_email="liuquan.frank@gmail.com",
    description="SenseVoice - Multilingual ASR Model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FunAudioLLM/SenseVoice",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 