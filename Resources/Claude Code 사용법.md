# Claude Code 사용법

## Claude Code란?

Claude Code는 Anthropic에서 만든 **CLI(명령줄) 기반 AI 코딩 어시스턴트**입니다. 터미널에서 직접 AI와 대화하며 코딩 작업을 수행할 수 있습니다.

---

## 기본 명령어

| 명령어 | 설명 |
|--------|------|
| `claude` | Claude Code 실행 |
| `claude --version` | 버전 확인 |
| `claude --help` | 도움말 보기 |

---

## 주요 기능

### 1. 파일 작업
- 파일 읽기/쓰기/편집
- 폴더 구조 탐색
- 코드 검색

### 2. Git 작업
- `git status` - 변경사항 확인
- `git add` - 파일 스테이징
- `git commit` - 커밋 생성
- `git push` - GitHub에 업로드
- `git log` - 커밋 이력 확인

### 3. 명령어 실행
- 터미널 명령어 실행
- 빌드, 테스트 등 자동화

### 4. 웹 검색
- 최신 정보 검색
- 문서 참조

---

## 유용한 요청 예시

```
"이 폴더의 구조를 설명해줘"
"git status 확인해줘"
"README.md 파일을 만들어줘"
"이 코드의 버그를 찾아줘"
"에이전트 오케스트레이션을 설명하는 다이어그램 만들어줘"
```

---

## Plan Mode

복잡한 작업 전에 **계획을 먼저 세우는 모드**입니다.

```
요청 → 계획 수립 → 사용자 승인 → 실행
```

실수를 줄이고 싶을 때 유용합니다.

---

## Git 활용 팁

### 커밋 ID 확인
```bash
git log --oneline
```

### 이전 버전 비교
```bash
# 별칭 사용
git diff HEAD~1 HEAD -- 파일명

# 커밋 ID 사용
git diff [이전커밋] [현재커밋] -- 파일명
```

### 특정 버전 파일 보기
```bash
git show HEAD~1:파일명
```

---

## 참고

- Claude Code 버전: `claude --version`으로 확인
- 도움말: `/help` 입력
- 피드백: https://github.com/anthropics/claude-code/issues
