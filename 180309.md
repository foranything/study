# 2018년 3월 7일

___

# ES6 (ES2015)

babeljs.io
esdiscuss
 
let 중괄호 단위

const 중괄호 단위

``` javascript
obj = {
	arr : [1,2,3]	
}

obj = []; //error
obj.arr.length = 0; // 됨
obj.arr.push(1); //됨
```

rest parameter

```
function foo (a, b, ... c) {
	console.log(c); //['c','d','e','f']
	console.log(Array.isArray(c)); // true ... arguments는 배열이 아님
}

foo('a','b','c','d','e','f');
```

#### spread operator

버터 바르는 거

```
var arr1 = [1,2,3];
var arr2 = [4,5,6];

var total = [...arr1, ...arr2] // [1,2,3,4,5,6]

function foo (a,b,c) {
	return a + b + c;
}

foo(...[1,2,3]) // 6
```

#### distructuring
```
var address = {
	city : 'new york'
	state : NY
}

var {city, state} = address;
city + ', ' state // new york, NY

var {city: c, state: s} = address;
c + ', ' + s //new york, NY

```

### default parameter
```
undefined 일떄

const s = 'ken'
`${s}`
```


const fn = (a) => {
	console.log(a);
};

익명 함수
 

