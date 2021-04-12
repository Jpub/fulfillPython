# 효율적 개발로 이끄는 파이썬 실천 기술
![효율적 개발로 이끄는 파이썬 실천 기술](http://image.kyobobook.co.kr/images/book/xlarge/872/x9791190665872.jpg)

**출판사** 제이펍  
**원서명** Python実践入門 ── 言語の力を引き出し、開発効率を高める(원서 ISBN: 9784297111113)  
**저자명** 스야마 레이  
**역자명** 김연수  
**출판일** 2021년 4월 9일 예정  
**페이지** 392쪽 예정  
**ISBN**  979-11-90665-87-2 (93000)  


[### 도서 소개 페이지 바로 가기 ###](https://jpub.tistory.com/)  


## <효율적 개발로 이끄는 파이썬 실천 기술> 샘플 코드

제이펍 <효율적 개발로 이끄는 파이썬 실천 기술>의 샘플 코드입니다.

이 샘플 코드는 Python 3.8.1, JupyterLab 1.2.4에서 동작을 확인했습니다.
각 디렉토리는 책의 장 이름에 맞춰져 있으며, 샘플 코드는 각각 하나의 노트북 파일(.ipynb)에 모아두었습니다.
노트북 파일을 실행할 때는 노트북 파일이 있는 위치에서 `jupyter lab` 명령어를 실행하기 바랍니다.

### 실행 방법

먼저 가상 환경 만들기와 JupyterLab을 설치합니다.

```shell
# 가상 환경 만들기와 JupyterLab 설치
$ python3 -m venv venv
$ . venv/bin/actiate
(venv) $ pip install jupyterlab==1.2.4
```

각 장에 해당하는 디렉터리에서 Jupyter Lab을 실행하면 브라우저가 실행됩니다.
왼쪽 패널에서 .ipyng 파일을 열면 샘플 코드가 표시됩니다.
소스 코드가 입력되어 있는 셀을 선택한 뒤, Shift + Enter를 누르면 해당 셀의 코드가 실행됩니다.

```shell
# 각 장의 노트북 파일이 있는 위치에서 JupyterLab을 실행
(venv) $ cd 01-introduction
(venv) $ jupyter lab
```

실행 화면 예시는 'screenshot_01.png'을 참조합니다.

