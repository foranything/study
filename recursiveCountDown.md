# 2018년 3월 12일

# recursive  countDown
``` javascript
function getElementByClassName (el,className) {
	var result = [];

	for (var i = 0; i < el.children.length; i++) {
		let childEL = el.children[i];

		if (childEl.classList.contains(className)) {
			reslt.push(childEl);
		}
		
		if (childEl.children.length){
			result = result.concat(getElementByClassName(childEl, className));
		}
	}

	return result;
}
```
