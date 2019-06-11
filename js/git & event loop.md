# 2018년 3월 7일
___

# git
___

git init 

git status

git add index.html

git commit -m “update index.html”

git log

git checkout develop

git checkout -b staging 브랜치 새로 만드는거

git branch 로컬 브랜치 보여 주는거

git push origin master

git pull origin master

git remote -v

git remote add hello https://aaaa

___
# Event Loop
___

Single-threaded 자바스크립트에서 콜스택이 하나임

V8 engine 크롬에서 쓰는거 (노드 js도)

Call stack

Callback queue

Asynchronous

Web API

___
V8 Engine

heap 메모리 

stack 콜 스택 
	함수가 실행 되면 스택에 들어갑니다.
	함수가 종료 되면 스택에서 빠져나갑니다.

web API 브라우저가 제공

callback queue 

evnet loop


[loupe](http://latentflip.com/loupe/?code=JC5vbignYnV0dG9uJywgJ2NsaWNrJywgZnVuY3Rpb24gb25DbGljaygpIHsKICAgIHNldFRpbWVvdXQoZnVuY3Rpb24gdGltZXIoKSB7CiAgICAgICAgY29uc29sZS5sb2coJ1lvdSBjbGlja2VkIHRoZSBidXR0b24hJyk7ICAgIAogICAgfSwgMjAwMCk7Cn0pOwoKY29uc29sZS5sb2coIkhpISIpOwoKc2V0VGltZW91dChmdW5jdGlvbiB0aW1lb3V0KCkgewogICAgY29uc29sZS5sb2coIkNsaWNrIHRoZSBidXR0b24hIik7Cn0sIDUwMDApOwoKY29uc29sZS5sb2coIldlbGNvbWUgdG8gbG91cGUuIik7!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D)


