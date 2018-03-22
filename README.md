# study

closure
``` javascript
for (var i = 1 ; i < 11 ; i++){
	(function (j){
		setTimeout(function foo () {
			console.log(j)
		}, j * 1000);
	})(i);
}
```
