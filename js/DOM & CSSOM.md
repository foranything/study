# 2018년 3월 2일
___

#### 이벤트 

```javascript

function onBoxClick (ev) {
	console.log(ev.target.id);
}

Element.addEventListener(‘click’, onBoxClick);


setTimeout(function () {

	Element.removeEventListener(‘click’, onBoxClick);

},3000);

```

___
#### DOM & CSSOM

Document Object Model

CSS Object Model

HTML

- markup언어 
  - marking up 
	- 원고를 작성할 떄, 어떤 식으로 인쇄 되어야 하는지에 관한 지시를 적는 행위
- 특정 기호나 단어를 사용하여 글의 서식, 구조, 그리고 스타일을 정해 주는 언어

CSS

- Cascading Style Sheets
- 폭포수처럼 흘러내리는 ?
- 스타일 속성이 상위 노드에서 하위 노드로 상속되는 습성이 있다.

| 스타일          | 점수 |
| ----- | -----:|
| inline style|1000pt|
| id selector	|100pt|
| class attribute pseudo 	|10pt|
| element, pseudo-element |1pt|

*{} === 0점

li:first-line {} 2점 pseudoElement

ul ol+li 3점

h1 + *[rel=up] {} 11점

li.red.level {} 21점

___

#### Rendering Process

바이트
->
캐릭터
->
토큰
->
노드
->
DOM

css도 html 비슷하게 만들어지고 합쳐지면 
**Render Tree**


#### Layout

viewport 

디바이스 폭 고려해서 어떻게 보여 줄지


#### painting 

실제로 그리는거

개발자 도구 -> 퍼포먼스 -> 녹화

#### Render Blocking Resources

html css 없으면

사실상 쓸모없는 화면

따라서 html css 를 Render Blocking Resource 라고 부름

css 는 html 상위에 넣음 (javascript는 cssom이 완성 되기 전에는 실행 시키지 않음)

script 태그 만나서 실행 하는동안 DOM Construction 멈춤

css 헤드에, 자바스크립트는 바디 최하단

#### Critical Rendering Path

최적화 시키는 작업 CRP

최대한 빠르고 효율적으로 보여주게 하기 위한 과정

