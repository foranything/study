# 2018년 2월 28일

___
```javascript

function findDulicates (arr) {
	if (arr.length){
		return [];
	}

	var result = [];
	var storage = {};

	for (var i = 0 ; i < arr.length; i++){
		if (!storage[arr[i]]){
			storage[arr[i]] = true;
		} else {
			result.push(arr[i]);	
		}
		
	}

	return result;
}

// 타이머
for (var i = 1 ; i < 11 ; i++){
	(function (j){
		setTimeout(function foo () {
			console.log(j)
		}, j * 1000);
	})(i);
}

```

___

[GeeksforGeeks](http://www.GeeksforGeeks.org)
___


# AJAX

##### Asynchronous Javascript And XML

**xhr** ? XMLHttpRequest

개념 - 데이터 교환 방식 (리로딩 없이 일부만 수정)

나중에 실행 되는거

EVENT LOOP 


##### Request Methods

- GET 정보를 달라! 
- POST 정보를 만들라!
	- 사용자 정보
- PUT 정보를 수정하라!
- DELETE 정보를 지우라!


##### HTTP Response
###### Response Code
- 1XX (무시)
- 2XX 성공적!
- 3XX 저쪽으로 가보세요! redirect
	- 301 영구적으로 옮겨짐
- 4XX 니 잘못! 
- 5XX 내 잘못..ㅠㅠ server error


##### JSON 
###### Javascript Object Notation

자바스크립트 오브젝트 처럼 쓰는 노테이션
자바스크립트는 아님

{
	“키” : “값”
}

string, number, object, array, boolean, null

``` javascript
$.ajax({
	url : ‘’,
	type: ‘GET’,
	success : function onData (a, b, c){ 
		console.log(c.state)
	},
	error: function onError (error){
	}
});
```



