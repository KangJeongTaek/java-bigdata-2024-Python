# file : p41_naverNewsApp.py
# desc : PyQt5,QtDesigner naver API 연동 뉴스검색 앱 만들기

import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from naverSearch import NaverSearch
import webbrowser
import datetime
import time

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self): # UI 파일을 로드해서 화면 디자인
        self.setWindowIcon(QIcon('./images/newspaper.png'))
        uic.loadUi('./day06/naverNews.ui',self)
        self.btnSearch.clicked.connect(self.btnSearchClicked) #버튼 서치 클릭시 처리
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked) #검색버튼 시그널 함수 연결
        self.tblSearchResult.cellDoubleClicked.connect(self.tblResultDoubleClicked) # 셀 더블 클릭시 처리

        self.show()

    def tblResultDoubleClicked(self): #셀 클릭시 처리
        selectRow = self.tblSearchResult.currentRow() #현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow,1).text()
        webbrowser.open(url) # 웹브라우저에서 열기

    def btnSearchClicked (self): #버튼 서치 클릭시 처리
        searchWord = self.txtSearchWord.text().strip()
        if len(searchWord) == 0: #Validation Check(입력 검증)
            QMessageBox.about(self,'네이버검색','검색어를 입력해주세요')
            return # 함수 탈출
        else:
            pass
        #QMessageBox.about(self,'네이버검색','검색시작!!!')
        #검색 시작
        api = NaverSearch() #api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        # print(jsonSearch)
        self.makeTable(jsonSearch) # 검색 결과로 리스트뷰를 만드는 함수 호출


    def makeTable(self,data):
        result = data['items'] # 네이버 검색 결과의 키 items의 값들만 활용
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result)) # 10개면 10개
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목','뉴스링크','게시일자'])
        n = 0
        for post in result:
            #html 태그, 특수문자 삭제를 해야 한다.(<b>손흥민</b>,&lt;[<],&gt;[>],&quot;["],&nbsp;[ ])
            title = str(post['title']).replace('<b>','').replace('</b>','').replace('&quot;','"').replace('&quot','"').replace('&nbsp','')
            self.tblSearchResult.setItem(n,0,QTableWidgetItem(title))
            self.tblSearchResult.setItem(n,1,QTableWidgetItem(post['link']))
            #현재날짜 Thu, 29 Feb 2024 09:00:00 +09:00로 변경하는 작업
            tempDates = str(post['pubDate']).split(' ') #tempDates라는 변수에 ['Thu,' ,29','Feb','2024','09:0:00', '+0900']
            year = tempDates[3]
            month = time.strptime(tempDates[2],'%b').tm_mon #Feb, Mar 같은 달의 영어 이름을 2,3과 같은 숫자로 변경하는 로직
            month = f'{month:02d}' # 월을 두 자리로 만들 때
            day = tempDates[1]
            date = f'{year}-{month}-{day}'
            self.tblSearchResult.setItem(n,2,QTableWidgetItem(f'{date}'))
            n += 1
            self.tblSearchResult.setColumnWidth(0,430) #QTable에 가로 스크롤 없애기 위해 넓이 조절
            self.tblSearchResult.setColumnWidth(1,200)
            self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 더블클릭 금지
            

    def closeEvent(self, QCloseEvent): # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if re == QMessageBox.Yes: #진짜 닫음
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            QMessageBox.about(self,'취소','종료하지 않습니다.')

app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행
