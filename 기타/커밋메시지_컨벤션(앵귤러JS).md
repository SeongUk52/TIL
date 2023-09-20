# Commit Message Conventions

[AngularJS Git Commit Message Conventions](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)

---
📄커밋 메시지 형식
```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

## Subject line

### < type>

- feat: 기능
- fix: 버그 수정
- docs: 문서
- style: 서식, 세미콜론 누락,...
- refactor: 래펙터링
- test: 누락된 테스트 추가 시
- chore: 유지보수

### < scope>
- 커밋 변경 위치를 지정하는 모든 것 (ex: $location, $browser, $compile, $rootScope, ngHref, ngClick)

### < subject>
- 명령형, 현재시제 사용
- 첫 글자를 대문자로 표시하지 마라
- 끝에 점(.) 찍지 마라

## Message body
- 명령형, 현재 시재 사용
- 변화에 대한 동기와 커밋 이전과의 상태 변화를 포함

## Message footer
- BREAKING CHANGE : 중대한 변경점
- 모든 호환성이 손상되는 변경은 변경, 근거 및 마이그레이션 메모에 대한 설명과 함께 바닥글에 언급되어야 함
