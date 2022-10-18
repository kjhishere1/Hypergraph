# Hypergraph

<details>
<summary>소개</summary>

## 1. Who
부산동성고등학교 1학년 6반 김준형이 만듦.

## 2. When
개발 기간 `2022-10-10 ~ 2022-10-11` 약 3시간 소요함.

## 3. Where
**`지속 가능한 발전`** 이라는 주제에 어울리게 [Github](https://namu.wiki/w/GitHub)에 코드를 올려 누구나 자유롭게 접근하고, 기능을 추가하거나 바꿀 수 있게 함.

## 4. What
`Hypergraph`.
정보 시간에 배운 [Turtle](https://docs.python.org/ko/3/library/turtle.html) 모듈을 활용해 좌표평면을 그리고, 직접 함수를 작성하여 좌표평면에 그리는 프로그램을 작성함.

## 5. How
정보 시간에 배운 [Python](https://www.python.org)과 [Turtle](https://docs.python.org/ko/3/library/turtle.html)을 활용하여 만듦.
Hypergraph는 Class를 이용하여 만들었고, 내부에 `_move` 함수나 `drawX` 등의 함수를 작성하여 처리함.

## 6. Why
수학시간에 배운 이차함수를 [Turtle](https://docs.python.org/ko/3/library/turtle.html)에서 구현 해 보는것을 목적으로 만들었음.
예전에 스크래치로 비슷한 것을 만들어 봤는데 괜찮지 않은 결과물이 나와서 신경쓰였음.


# 설명
파일은 `hypergraph.py`와 `run.py`로 총 두가지 파일로 쓰여져 있음.

`hypergraph.py`는 좌표평면과 함수 그리기를 위한 코드를 모았고, 그 모아진 코드를 사용자가 이용하기 쉽게 기능을 추가한 것이 `run.py`임.
</details>

## hypergraph.py
`hypergraph.py`는 `turtle` 모듈만을 사용함.

클래스 `Hypergraph`의 `__init__` 함수는 `Hypergraph` 클래스 내부에서 사용할 함수를 클래스가 정의될 때 선언함.

<details>
<summary>설명 접기/펼치기</summary>

### \_\_init\_\_ 함수
**`self.function`** 은 클래스가 인자로 받은 함수를 함수 내에서 사용하기 위해서 설정함.

**`self.step`** 은 함수에 x값을 넣어서 y값을 구하고, 이 좌표를 모두 모아서 그리면 너무 느려지기 때문에, `step`의 배수를 x값에 넣는다는 뜻임.

**`self.width`** 와 **`self.height`** 는 `turtle` 창의 크기를 정함.
창 크기 이상의 좌표평면을 그리면, 시간이 오래걸리고 비효율적이기 때문임.

**`xMax`** 와 **`yMax`** 는 x, y 범위의 최댓값이고,
**`xMin`** 과 **`yMin`** 은 x, y 범위의 최솟값임.

**`self.xList`** 는 x의 범위 내에서 step의 배수를 만족하는 모든 x값의 집합임. 이 집합의 값으로 y값을 구해 좌표를 정함.

### _screenSetup 함수
`Turtle` 창의 크기를 정하고, screen을 돌려줌.

### _turtleSetup 함수
그래프를 그릴 `Turtle` 을 불러오고,
커서를 숨기고, 속도를 최댓값으로 설정 한 후 `turtle`을 돌려줌.

### _move 함수
선을 그리지 않고 (`penup`) x, y 좌표로 이동 한 후에 펜을 내림 (`pendown`)

### originMark 함수
원점에 `O`를 표기함.

### drawX 함수
X축을 그림.

### drawY 함수
Y축을 그림.

### contourX 함수
(0, 0)으로 이동 후, grad를 기준으로 눈금을 X축에 새김

### contourY 함수
(0, 0)으로 이동 후, grad를 기준으로 눈금을 Y축에 새김

### _BetterRange 함수
`start`에서 `stop`까지 `step` 만큼의 리스트를 줌. \
`range`함수는 30에서 -30까지의 리스트가 작동하지 않음.

### _drawFunc 함수
입력 받았던 함수 식을 토대로 x 정의역의 수를 함수에 넣어서 `turtle`을 이동시킴.

### Graph 함수
`_drawFunc`을 멈추지 않고 이어서 그림.
</details>

## util.py
`util.py`는 `run.py` 에서 사용되는 함수를 모은 모듈임.

<details>
<summary>설명 접기/펼치기</summary>

### logo 변수
HYPERGRAPH 글자를 ASCII 아트로 나타낸 것.

### logo_c 변수
HYPERGRAPH 글자를 ASCII 아트로 나타낸 것. \
`rich`에서 사용하기 위해 수정됨.

### pip_install 함수
없는 모듈을 다운 받는다. 리스트로 넣을 시 여러 모듈을 한꺼번에 받는다. \
`rich` 모듈을 사용하기 위해 만듦.

### makeTable 함수
설정을 보여주는 Table을 리턴한다. \
`rich` 모듈을 사용하여 만듦.
</details>

## run.py
`run.py`는 `hypergraph.py` 를 쉽게 사용하기 위해 만든 실행용 코드.

<details>
<summary>설명 접기/펼치기</summary>

</details>