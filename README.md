# 세종대 맛집 추천 서비스 세종냠냠
#### 2021년 7월 10일부터 2021년 7월 16일까지 진행된
#### 세종대학교 - 건국대학교 교류전에서 제작한 프로그램입니다.

------------

### 사용 언어
* django, html, css, javascript, SQLite3

### 프로그램 소개

#### 1. 메인페이지
* 메인페이지에서 맞춤 추천 받기를 클릭하면 설문페이지로 넘어갑니다.

![메인화면](https://user-images.githubusercontent.com/78775910/126878285-cb1695cc-4f43-4cce-a59b-5730df09927f.png)

#### 2. 설문페이지
* 질문은 4개로 구성되어 있으며 선택지를 고른 뒤, 맞춤 맛집 찾기 버튼을 클릭합니다.
* 모든 음식점 데이터 베이스를 순회하면서, 선택한 모든 조건에 충족하는 음식점을 우선 검색합니다.
* 만일 충족하는 음식점이 없으면 중요하지 않은 조건부터 삭제 수 재검색하게됩니다.
(ex. 반주하지 않는다면 술집까지 포함시켜서 재검색)
* 이 때 모든 질문에 답을 하지 않은 경우 경고창이 뜨며 결과페이지로 넘어가지 않습니다.
좌측 상단에 HOME 버튼을 클릭하면 메인페이지가 출력됩니다.

![설문화면](https://user-images.githubusercontent.com/78775910/126878309-1c24fa85-b815-4689-bf0f-22dac4deaf54.png)

#### 3. 결과페이지
* 선택지에 해당하는 맛집이 2개 이상이라면 랜덤으로 한 가지가 뽑혀서 출력됩니다.
* 결과페이지에서 출력되는 정보는 가게명, 가게 사진, 주소, 가격, 영업시간, 감성 여부, 동행인, 반주 여부가 있습니다.
* 다시 고르기 버튼을 클릭하면 설문페이지가 출력되며 결과페이지에도 HOME버튼을 넣었습니다.

![결과화면](https://user-images.githubusercontent.com/78775910/126878310-f94f13c0-baff-4017-8912-53ace0ed2ca7.png)
