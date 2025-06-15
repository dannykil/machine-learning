from setuptools import setup, find_packages

REQUIRED_PACKAGES = ['gcsfs>=2021.4.0']

setup(
    name='trainer',  # 패키지 이름 (PyPI에 배포할 경우 다른 패키지와 중복되지 않아야 함)
    version='0.2',  # 패키지 버전
    install_requires=REQUIRED_PACKAGES,
    # author='Your Name',  # 제작자 이름
    # author_email='your.email@example.com',  # 제작자 이메일
    # url='https://github.com/your_username/your_package_name',  # 패키지 홈페이지 주소 (보통 GitHub 저장소)
    packages=find_packages(),  # 패키지에 포함될 파이썬 패키지를 자동으로 찾아줌
    # description='My Training Application',  # 패키지에 대한 간단한 설명
    description='My Training Application with Arguments',
    include_package_data = True
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    # python_requires='>=3.6', # 요구되는 파이썬 최소 버전
)

# 패키지 생성
# python setup.py sdist --formats=gztar