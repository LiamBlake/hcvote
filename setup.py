from setuptools import setup

setup(
    name="Hare-Clark Vote Counter",
    url="https://github.com/LiamBlake/Hare-Clark-VoteCounter",
    author="Liam Blake",
    author_email="",
    packages=["hcvote"],
    install_requires=["pandas==1.3.3"],
    extras_require={
        "dev": ["black==21.9b0", "isort==5.9.3", "flake8==3.9.2"],
        "test": ["pytest==6.2.5", "pytest-cov==3.0.0", "pytest-order==1.0.0"],
    },
    version="0.1",
    license="GNU",
    description="Implementation of Hare-Clark voting system.",
    long_description=open("README.md").read(),
)
