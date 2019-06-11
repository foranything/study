# 2018년 3월 5일
___

#### Basic Git

git 

- unpleasant person 기분이 좋지 않은 사람
- 존재하지 않는 터미널 명령어, 그리고 그냥 발음할 수 있는 랜덤 세 글자
- global information tracker - 
- goddamn idiotic truckload of shit

버전 관리 시스템 

- 파일 변경 사항을 추적해주는 프로그램
- 협력 개발을 도와주는 프로그램
- 누가 언제 무엇을 수정 했는지 알 수 있게 해주는 프로그램
- 다시 과거 시점의 상태로 돌아갈 수 있게 해주는 프로그램

___

- 사용자가 코드와 그 코드의 히스토리를 사용자 컴퓨터에 보관 함
- 인터넷 접근이 필요 없음
- (클라우드에 있는 정보를 업데이트 하거나 받아 올때 제외)
___

#### snapshot

- git이 코드 히스토리를 기억하는 방식
- 주어진 시점에 파일들이 어떻게 생겼는지를 기록 한다.
- 시점은 우리가 선택하여 기록해 달라고 명령한다.
- 기록된 과거 시점으로 돌아가서 다시 볼 수 있다.
- 기록된 미래 시점으로 돌아가서 다시 볼 수 있다.

#### commit

- snapshot을 생성하는 행위
- 기본적으로 git 프로젝트는 수 많은 커밋들로 이루어져 있다.
- 각 커밋은 세가지 정보를 보관합니다
	1. 파일 변경 사항
	2. 바로 이전 커밋, 즉 parent commit
	3. 커밋 해쉬
		- 고유 아이디
- 변경사항을 스테이지에 올린다. (다음 커밋에 포함 하고 싶은 사항을 예약하는 것)
- git add 경로
- git add .


#### Repository

- 모든 파일들과 그 파일들의 히스토리가 모여 있는 곳
- 모든 커밋을 포함하고 있는 곳
- 개인 컴퓨터나 클라우드 서버(Github)에 있다.
- 클라우드에서 복사해서 다운 바든 행위를 clone이라고 한다.
- 클론을 함으로서 협업이 가능해 진다.
- 내 컴퓨터에 없는 내용을 클라우드로부터 추가적으로 다운로드 받는 행위 PULL이라고 한다.
- 내 컴퓨터의 변경 사항을 클라우드에 추가하는 행위를 PUSH 한다고 한다.

#### Branch

- commit 들은 branch 내에 존재 한다.
- git에서 메인 브랜치는 master branch.

##### HEAD

현재 branch 의 마지막 commit
여러가지 경우가 많지만, 일단 잘 모르겠다면 패스

#### master

가장 중심이 되는 branch


git remote -v 리모트 저장소 목록 보기
git remote add remote_nmae remote_url 리모트 저장소 추가하기

git commit — amend 이전 커밋에 그냥 추가해 버림

checkout -b develop 브랜치 만들고 이동

___
# 2018년 4월 18일
___

# git introduction 

#### < local vs remote >
##### Local : your computer
##### Remote: Storage in Cloud

###### 리모트 추가
```
git remote add origin http://name.git
git remote remove REMOTE_NAME REMOTE_URL
```
###### 리모트 보기
```
git remote -v
```
###### 브랜치 생성 && 이동
```
git checkout -b BRANCH_NAME
```
###### 브랜치 삭제
```
git branch -d BRANCH_NAME

//강제 삭제
git branch -D BRANCH_NAME
```
###### 브랜치 병함
``` 
//on master일 떄
git merge dev //하면 마스터로 dev를 갖다 붙임
```

##### reset

mixed // add 안된 상태로
soft // add 된 상태로
hard // 날려 버림
