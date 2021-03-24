from setuptools import setup, find_packages


setup(
    name='pythonbook',
    version='1.0.0',
    packages=find_packages(),

    # 저작자, 프로젝트 정보
    author='rei suyama',
    author_email='rhoboro@gmail.com',
    url='https://github.com/rhoboro/pythonbook',

    # 짧은 설명문과 긴 설명문을 준비
    # content_type은 다음 중 선택
    # text/plain, text/x-rst, text/markdown
    description='This is a test package for me.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # 파이썬 버전은 3.6 이상, 4 미만
    python_requires='~=3.6',

    # PyPI 상에서의 검색, 열람을 위해 이용되는 
    # 라이선스, 파이썬 버전, OS를 포함시킴
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Operating System :: OS Independent',
    ],
    install_requires = [
        # Click 버전은 7.0 이상 8 미만
        'Click~=7.0',
        # sampleproject의 커밋을 지정해서 얻음
        'sampleproject@git+https://github.com/pypa/sampleproject#sha1=0754c8ab224f0886f4939cca3f4ca9e5fd5e5d90',
    ],
    extras_require = {
        's3': ['boto3'],
        'gcs': ['google-cloud-storage'],
    },
    package_data={'pythonbook': ['data/*']},
)