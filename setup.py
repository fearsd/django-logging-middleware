import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-logging-middleware", # Replace with your own username
    version="0.1.2",
    author="Rifat Fazlutdinov",
    author_email="rifatfazlutdinov@gmail.com",
    description="A small package to log django requests and responses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fearsd/django-logging-middleware",
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=["django>=3.0", "loguru"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1"
    ],
    python_requires='>=3.6',
)
