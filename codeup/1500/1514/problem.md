# 1514 : 레이저 체스
  
## 문제 설명    
맨사들이 주로 즐겨 한다는 레이저 체스 게임.

레이저 체스는 레이저 장기라는 이름으로 더 지니어스의 데스매치 게임으로 나오기도 했다

그 레이저 체스에는 스플리터라는 장치가 있다

0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 
이렇게 7∗7의 판이 있다고 하자.

여기에 화살표 방향으로 레이저를 쏘면, (레이저는 1로 표시)

 0 0 0 0 0 0 0
 0 0 0 0 0 0 0
 0 0 0 0 0 0 0
 1 1 1 1 1 1 1  --> 레이저 방향
 0 0 0 0 0 0 0
 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 
이렇게 된다.

그런데 중간에 스필리터를 끼워 넣으면, (스플리터는 2로 표시)

 0 0 0 1 0 0 0
 0 0 0 1 0 0 0
 0 0 0 1 0 0 0
 1 1 1 2 1 1 1
 0 0 0 1 0 0 0
 0 0 0 1 0 0 0
 0 0 0 1 0 0 0
이렇게 레이저가 위/아래로 분산된다.

맵안에는 스필리터가 3개 있고, 4번째 줄에 레이저를 쏜다고 했을 때 맵의 상태를 출력하시오.

## 입력
세 줄에 걸쳐 (행, 열)의 형태로 스플리터 위치가 입력된다.

## 출력
스플리터가 각 레이저를 분산했을때 레이저가 차지하는 부분을 1로 레이저가 차지하지 않는 부분을 0 스플리터를 2으로 하여 7∗7의 맵을 출력하라

## 입력 예시   
2 4
4 4
6 4

## 출력 예시
0 0 0 1 0 0 0 
1 1 1 2 1 1 1 
0 0 0 1 0 0 0 
1 1 1 2 1 1 1 
0 0 0 1 0 0 0 
1 1 1 2 1 1 1 
0 0 0 1 0 0 0 