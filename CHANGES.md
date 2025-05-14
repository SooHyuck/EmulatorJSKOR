# 변경 사항

# 4.2.1
이것은 버그 수정 전용 릴리스입니다.

- 코어 가져오기 안전장치가 이제 고정된 버전을 가져옵니다 ([@gantoine](https://github.com/n-at) 덕분에).
- 아케이드 코어의 비디오 회전 수정 (@allancoding](https://github.com/allancoding) 덕분에)
- 코어 간 전환을 수정했습니다.
- 변경: 이제 로컬 저장소 설정이 시스템별이 아닌 게임별로 저장됩니다.
- C-다운에 대한 게임패드 입력을 수정했습니다.
- RetroArch가 항상 저장이 `.srm`이라고 가정하는 것을 수정했습니다.
- EJS 종료 이벤트 수정
- 지원되지 않는 경우 “저장 파일 저장/로드” 버튼을 숨깁니다.
- 핵심 목록의 순서를 수정했습니다.
- 바이오스/부모/패치 파일 배치 동작을 수정했습니다.
- rar 압축 해제 수정.
- 피코드라이브 코어(`sega32x`) 수정.
- 리브레트로-UAE 코어(`amiga`)를 수정했습니다.

# 4.2.0 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/8d42d53d4fdf0166f71eaa07529cadf93350b76e)
제 생각에는 이번 릴리스가 한동안 있었던 릴리스 중 가장 안정적인 릴리스입니다. 이번 릴리스에 추가된 많은 기능은 일부 버그를 수정하는 과정에서 부수적으로 추가된 것입니다.

- 동일한_cdi 코어가 압축된 바이오스 파일을 직접 처리하도록 함 (@pastisme](https://github.com/pastisme) 덕분에)
- 오디오 슬라이더/음소거 버튼 수정 (@n-at](https://github.com/n-at) 덕분에)
- 동영상 회전 기능 추가 ([@allancoding](https://github.com/allancoding) 덕분에)
- 페르시아어 `fa-AF` 언어 추가 ([@iits-reza](https://github.com/iits-reza) 에게 감사드립니다).
- 게임 시작 오류에 대한 더 많은 캐치 추가
- 기본 webgl2 옵션 수정
- 항목을 하위 메뉴로 나누어 설정 메뉴를 구성했습니다.
- 에뮬레이터JS 종료 버튼 수정
- 내부적으로 구성 가능한 retroarch.cfg 변수를 추가하는 기능을 추가했습니다.
- 기본 설정이 로컬 저장소에 저장되는 문제 수정
- 브라우저 SRM 저장에서 수정됨(최종)
- 웹어셈블리 메모리에서 저장 상태 읽기
- PPSSPP 에셋 로드 시 문제 수정
- 내부 다운로드 파일 함수를 콜백 기반이 아닌 프라미스 기반으로 리팩터링했습니다.
- 코어에 스레드 또는 webgl2가 필요한지 확인하는 기능이 추가되었습니다.
- 설정 메뉴에서 코어 간 전환 기능 추가
- SharedArrayBuffer 가 정의된 경우 스레드를 활성화/비활성화하는 기능을 추가했습니다.
- 컨트롤 세팅 메뉴에 PSP 컨트롤러 구성표를 추가했습니다.
- 파이어폭스에서 볼륨 슬라이더 배경 높이를 수정했습니다.
- 라이트건 디바이스에 대한 처리 추가
- EmulatorJS `build-emulatorjs.sh` 빌드 스크립트를 리팩터링했습니다.
- ppsspp` 코어 추가

# 4.1.1 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/4951a28de05e072acbe939f46147645a91664a07)
- 2xScaleHQ 및 2xScaleHQ 셰이더 수정 ([@n-at](https://github.com/n-at) 에게 감사드립니다).
- 베트남어(`vi-VN`) 추가 (@TimKieu](https://github.com/TimKieu) 덕분에)
- PUAE 코어에 대한 CUE 생성 비활성화 ([@michael-j-green](https://github.com/michael-j-green) 덕분에)
- 독일어 번역 업데이트 ([@jonas0b1011001](https://github.com/jonas0b1011001) 덕분에)
- 번역할 누락된 호출 추가 ([@angelmarfil](https://github.com/angelmarfil) 덕분에)
- 터키어 (`tr-TR`) 추가 ([@iGoodie](https://github.com/iGoodie) 에게 감사드립니다).
- 일부 구형 브라우저에 대한 게임패드 지원 수정 ([@ZhaoTonggang](https://github.com/ZhaoTonggang) 에게 감사드립니다).
- 저사양 코어에서 기본값이 webgl1로 변경되었습니다.
- webgl1과 webgl2 사이를 전환하는 기능이 추가되었습니다.
- 에뮬레이터JS와의 코어 호환성 확인.
- 오른쪽 클릭 메뉴에 코어 라이선스 추가.
- 모두 대체`의 사용법을 제거했습니다.
- 게임 시작 충돌시 설정을 변경하는 기능을 추가했습니다.
- 파일을 올바르게 종료하고 저장하기 위해 '종료'버튼을 추가했습니다.
- 모바일 장치에서 마우스 수정.
- 모듈화 된 에뮬레이터 JS.
- WHLoader hdf 롬 수정.
- 파일` 객체에 대한 지원이 추가되었습니다 ([@pastisme](https://github.com/pastisme) 덕분에).

# 4.0.12 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/c3ba473d1afc278db136f8e1252d0456050d6047)
- 스크롤 막대 CSS 수정([@allancoding](https://github.com/allancoding) 덕분에)
- 페이지 밖으로 나가는 대신 컨텍스트 메뉴 뒤집기
- 파일 저장용 후크 추가 (@gantoine](https://github.com/gantoine) 덕분에)
- 각 가상 게임패드 버튼에 클래스 추가
- EJS_forceLegacyCores` 옵션 추가
- EJS_noAutoFocus` 추가 (고급 개발자에게만 해당되며, 여러분이 사용할 옵션은 아닙니다.)
- 지원되는 Amiga 파일 확장자 추가 ([@michael-j-green](https://github.com/michael-j-green) 덕분에)
- M3U 목록 사용시 ROM / 디스크의 파일 이름 표시 ([@michael-j-green](https://github.com/michael-j-green) 덕분에)
- vsync 옵션 추가
- 고급 셰이더 구성 지원 추가 ([@n-at](https://github.com/n-at)에게 감사드립니다).

# 4.0.11 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/cafd80d023afa9562c7054e89a4240f3381d64ff)
- EJS_disableLocalStorage`를 사용하여 로컬 스토리지를 비활성화하는 기능을 추가했습니다. (@n-at](https://github.com/n-at)에게 감사드립니다.
- 기간으로 `EJS_emulator.displayMessage`를 트리거하는 기능을 추가했습니다. ([@allancoding](https://github.com/allancoding)에게 감사드립니다.)
- 이제 `EJS_emulator.gameManager.getState`가 프로미스 대신 Uint8Array를 반환합니다.
- 4.0.10 릴리스에서 깨진 저장 상태를 수정했습니다.

# 4.0.10 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/390605d2ab48db16c07c8fb4fc2815033af5c3a6)
- 컨트롤 입력이 중복되는 버그를 수정했습니다.
- 모바일 설정 메뉴 위치를 수정했습니다.
- 와즘 인스턴스에 사용자 정의 파일을 로드하는 기능.
- mame2003` 시스템의 이름을 `mame`으로 변경했습니다.
- mame2003` 코어에서 mame 면책 조항을 제거했습니다.
- C64, C128, VIC20, Plus/4, PET용 VICE 코어 추가([@michael-j-green](https://github.com/michael-j-green) 덕분에).
- 팝업 본문과 버튼 사이에 패딩을 추가했습니다.
- 캐시된 데이터베이스를 비활성화하는 기능을 추가했습니다.
- 일부 코어의 스크린샷을 수정했습니다.
- 전체화면 이후 게임 요소에 초점이 맞지 않던 현상을 수정했습니다.
- 누락된 패미컴 컨트롤을 추가했습니다.
- 볼륨 슬라이더 그림자를 수정했습니다. ([@allancoding](https://github.com/allancoding) 에게 감사드립니다.)

# 4.0.9 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/ddb5c6092f12a63a46d74ea67e6469726665ebc2)
- 리포지토리 기록 재작성 - 더 빠른 복제 시간을 기대하세요.
- Vice64가 큐 파일을 생성하지 못하도록 방지 ([@michael-j-green](https://github.com/michael-j-green) 덕분에)
- 중국어 번역 업데이트 (@oyepriyansh](https://github.com/oyepriyansh) 덕분에)
- 컨텍스트 메뉴를 여는 버튼 추가 ([@andrigamerita](https://github.com/andrigamerita)에게 감사드립니다).
- 오른쪽에 있는 항목의 메뉴바 텍스트 배치를 수정했습니다.
- 사파리에서 전체 화면에서 게임 요소의 크기가 조정되지 않던 버그를 수정했습니다.
- 초기 페이지 로딩 시 하단 메뉴가 표시되던 버그를 수정했습니다.
- 게임 이름이 설정되어 있을 때 게임 롬 파일명이 “게임”으로 표시되던 문제를 수정했습니다.
- 웹글루2를 지원하지 않는 브라우저를 위한 레거시 닌텐도 64 코어를 추가했습니다.

# 4.0.8 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/f579eb4c080f612723fd6a119b02173cafb37503)
- 가상 게임 패드 dpad의 오타를 수정했습니다.
- 업데이트된 데스뮴 코어를 추가했습니다.
- 키 매핑 수정 (@allancoding](https://github.com/allancoding) 덕분에).
- 애드블록 메시지 수정 (@allancoding](https://github.com/allancoding) 덕분에).
- EJS_startButtonName` 옵션을 추가했습니다.
- 저장 상태를 드래그 앤 드롭하는 기능을 다시 추가했습니다.
- 치트 메뉴 수정.
- 게임이 실행되지 않는 경우 Safari 모바일 사용자를 위한 팝업 메시지를 추가했습니다.
- EJS_softLoad` 옵션을 추가했습니다.
- 아미가 코어를 추가했습니다.
- c64 코어를 추가했습니다.

# 4.0.7 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/f579eb4c080f612723fd6a119b02173cafb37503)
- 되감기 기능 추가 ([@n-at](https://github.com/n-at) 덕분에)
- 감속 기능 추가 ([@n-at](https://github.com/n-at) 덕분에)
- 설정 메뉴 앞의 “구역” 개체를 수정했습니다.
- 가상 게임 패드 정렬을 수정했습니다.
- 'EJS_fullscreenOnLoaded' 옵션을 추가했습니다.
- 컨트롤 메뉴에 가상 게임패드 토글 추가(터치스크린 기기의 경우).
- 게임패드 ID가 “정의되지 않음”으로 표시되는 문제 수정.
- 스레드 코어를 추가했습니다.
- 조이스틱 번역을 추가했습니다([@allancoding](https://github.com/allancoding) 덕분에).
- 전체 화면 버튼 툴팁 수정 (@allancoding](https://github.com/allancoding)에게 감사드립니다).
- 터보그래픽스-16, 슈퍼그래픽스, PC 엔진, 네오 지오 포켓, 원더스완, PC-FX, 콜코비전 지원을 추가했습니다. (@n-at](https://github.com/n-at) 덕분에)
- 큐 파일 로딩 수정 (@n-at](https://github.com/n-at) 덕분에).
- 볼륨 슬라이더 숨기기 기능을 수정했습니다 ([@n-at](https://github.com/n-at) 덕분에 ).
- 새로운 mame2003_plus 코어 추가 (이제 기본 mame2003 코어).
- 레이블 대신 키코드 사용 ([@allancoding](https://github.com/allancoding) 에게 감사드립니다).

# 4.0.6 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5e338e7a888480cea331f6d4656bc8986a7d6b28)
- iOS 사파리에서 n64 수정
- 아타리2600, 아타리7800, 링스, 재규어, VB, 3도용 가상 게임패드 (@n-at](https://github.com/n-at) 덕분에)
- GBA, VB, 3도, 아타리2600, 아타리7800, 링스, 재규어용 컨트롤 버튼 (@n-at](https://github.com/n-at)에게 감사드립니다.
- EJS_controlScheme` 추가 ([@n-at](https://github.com/n-at) 덕분에)
- 빨리 감기 추가

# 4.0.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5307e6294ed9df5daabd6958b2b307bae01f59f1)
- pcsx_rearmed` 코어 추가
- pcsx_rearmed` 코어를 기본 `psx` 코어로 만들었습니다 (호환성 향상).
- fbneo` 코어 추가
- fbneo` 코어를 기본 `아케이드` 코어로 만들었습니다 (호환성 향상).
- 피코드라이브 코어 추가 (sega32x)
- 문서 정리
- rar 압축 해제 수정/업데이트
- segaMD, segaCD, sega32x 버튼 레이블 및 가상 게임 패드 추가 (@n-at](https://github.com/n-at) 덕분에)
- 스레드 사용 기능 추가 (사전 컴파일된 코어는 아직 사용할 수 없음).
- 게임패드 버튼 이벤트가 뒤바뀌는 현상을 수정했습니다(아래쪽은 위쪽, 위쪽은 아래쪽).
- 게임패드 축 릴리스가 트리거되지 않는 문제 수정
- 하이 베타 *** PSP 코어 추가-readme 참조

# 4.0.4 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/41491a738cf92ef9cee7d53f323aa2ab9732c053)
- 치트 “X” 버튼 수정
- 메모리 사용량 최적화
- 필요한 경우 URL을 blob/arraybuffer/uint8array로 설정하는 기능 추가

# 4.0.3 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5219ab51227bc0fb60cbc7b60e476b0145c932c9)
- RetroArch 메시지 제거
- 상단 중앙 비디오

# 4.0.2 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/06fe386e780bb55ef6baa4fbc6addd486bee747a)
- 정보 페이지에 RetroArch 라이선스 링크 추가
- 레거시 브라우저에 대한 게임패드 지원 수정

# 4.0.1 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/efbb9dd462ee0e4f2120a6947af312e02fcf657c)
전체 애플리케이션 재작성. 모든 것이 변경되었습니다. 주목해야 할 몇 가지 변경 사항은 다음과 같습니다:
- 작은 화면에 최적화.
- 더 이상 죽은 코드가 없습니다.
- 파이어폭스용 게임패드 수정.
- 브라우저에 srm 저장.
- srm 파일 가져오기/내보내기 기능.
- 더 이상 오래된 코어가 없습니다.

그리고 훨씬 더 많은 것이 변경되었습니다...

# 3.1.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/f7fa5d41487a424233b40e903020455606d68fee)
- iPad용 iOS 버그 수정
- 넷플레이가 추가되었습니다! (구형 코어에서만 작동)

# 3.1.0 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/614f5cb55e2768199ba05b756b47d0ab7ab283fd)
- 저장 상태를 드래그 앤 드롭하는 기능을 추가했습니다.
- 일부 '업데이트' 및 '취소', '닫기' 버튼의 혼동 수정
- 저장 상태 검색 메시지 제거
- 베타 넷플레이 정리(아직 작동하지 않음)
- (이론적으로) iOS 디바이스에서 워를 허용하지 않는 버그 수정

# 3.0.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/44c31371fb3c314cd8dea36ccbaad89fb3ab98e6)
- getUserMedia API를 지원하지 않는 디바이스에서 화면 녹화를 수정했습니다.
- 닌텐도 64 가상 게임패드에 C 레이블 버튼을 추가했습니다.
- EJS_color 버그를 수정했습니다.
- 저장 상태가 항상 올바르게 유지되도록 코어 자체에서 가져옵니다.
- 몇 가지 새로운 코어. (a5200, beetle_vb, desmume2015, fbalpha2012_cps1, fbalpha2012_cps2, fceumm, gambatte, mame2003, mednafen_psx, mednafen_psx_hw, melonds, mgba, mupen64plus_next, nestopia, snes9x).
- 가상 게임패드용 D-패드.
- 새로운 메뉴 옵션을 포함하도록 번역 파일을 업데이트했습니다.
- 가상 게임패드에 둘 이상의 구역 개체를 추가할 수 있습니다.
- 사용자 지정 메뉴 옵션을 설정하는 기능이 추가되었습니다.
- 가상 게임패드 왼손잡이 모드.
- 화면 녹화 svg를 수정했습니다.
- svg 아이콘 업데이트.
- 캐시 '모두 지우기' 버튼.
- 캐시 버튼이 메뉴 표시줄로 이동했습니다.
- 콘텐츠 길이를 사용할 수 없을 때 현재 다운로드한 크기를 표시하는 기능이 추가되었습니다.

# 2.3.9 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/088942083e44510f07133f2074a2d63a8af477cd)
- 업데이트 바이오스 다운로드 데이터 콜백 시 잘못된 변수 참조를 수정했습니다.
- 롬 저장소 크기 제한을 수정했습니다.
- 일부 파일에서 다운로드 퍼센트가 표시되지 않는 문제를 수정했습니다.

# 2.3.8 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5f176b963e4b2055983b82396378d1e3837a69c4)
- 깨진 셰이더를 제거합니다.
- 다운로드 퍼센트 메시지 추가.
- UI “저장 상태” 메시지가 사라지지 않는 문제를 수정했습니다.

# 2.3.7 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/8b9607becfe0aaad42b8b8486c7d379821b72125)
- 셰이더를 더 추가합니다.
- 사용자 지정 가상 게임패드 설정에 굵은 글꼴 크기 옵션을 추가합니다.
- 더 이상 현지화 파일에서 “normalOptions”를 설정하지 않습니다.

# 2.3.6 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/b2919bc2c3d2d4c9fe3ab4f4486790a376b7acfe)
- 게임패드에 대한 기본 컨트롤 매핑을 제거했습니다.
- 더 많은 문자를 인식하도록 유효하지 않은 문자 정규식을 업그레이드했습니다.

# 2.3.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/a5a9916aba041e75ee73815376ed4fd2e22701bd)
- 파일 이름/게임 이름 설정에서 유효하지 않은 문자를 감지하고 대체하기 위해 정규식을 사용합니다.

# 2.3.4 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/45d982b6362cfd29cb2eda9721066e03893ba0d8)
- 새로운 아케이드 코어 추가.
- 패치 파일 게임 ID 세트 버그 수정.

# 2.3.4 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/45d982b6362cfd29cb2eda9721066e03893ba0d8)
- 새로운 아케이드 코어를 추가합니다.

# 2.3.3 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/11bddd5a4277aa04f80b941f05cc024b3de58bfc)
- loader.js의 버전을 합리적으로 수정했습니다.
- 불필요한 데이터 저장을 방지하기 위해 게임 ID를 반환하는 함수를 생성했습니다.

# 2.3.2 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/e9e017435f2c41c6c2b127024cc88ac51bdf04d9)
- 참조 오류 수정.
- 커스텀 가상 게임패드 프로세서에서 값이 0으로 설정되면 값이 누락된 것으로 표시되던 버그를 수정했습니다.

# 2.3.1 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/0fd6d58e2011fa1a39bd2e11ba3d2f177

# 2.3.0 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/2fd0f545285151524262cc799efef6d996d7c6c1)
- 가상 게임패드 UI를 커스터마이징하는 기능이 추가되었습니다.
- 시작 시 셰이더가 설정되지 않는 버그를 수정했습니다.

# 2.2.9 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/018c39d4065b866487f8f18ca88c9488eab69a6d)
- 5분마다 인덱싱된 DB에 저장 파일을 저장하는 기능을 추가했습니다.

# 2.2.8 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/9860d662d02b56417044cca11937448041d9cf43)
- 게임패드 핸들러를 다시 작성합니다.

# 2.2.7 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/c03d18990b6536c1503bba2c640dbc13db982bb3)
- 불필요한 FS 프록시 함수를 제거했습니다.

# 2.2.6 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/fd71b5dfc2bd44d8e1f0e7c6c7b3ee1a1127a696)
- FPS 카운터를 추가했습니다.
- GBA 코어 측면을 수정했습니다.

# 2.2.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/4b444ec23918149a6052807d778af82f79883c01)
- 커스텀 컨트롤 매핑을 설정하는 기능을 추가했습니다.
- 사용자 지정 기본 볼륨 값을 설정하는 기능을 추가했습니다.
- 게임 패드 축을 버튼, 게임 패드 가변 값과 비교하여 잘못된 값으로 수정했습니다.
- 메뉴/컨텍스트 메뉴 버튼을 숨기거나 표시하는 기능을 추가했습니다.
- 게임 URL을 다른 데이터 유형으로 설정하는 기능을 추가했습니다.

# 2.2.3 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/41eed05677b4927bd114613040bfe4572c92c4b4)
- 압축 파일 보관 해제 함수 참조를 수정했습니다.
- 압축 파일 헤더 감지를 업데이트했습니다.
- 넷플레이를 제거했습니다.

# 2.2.1 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/19980deb12c3f0790176db6fc7b8b2de4069bf4e)
- 새로운 코어에 대한 코어 메뉴 옵션을 추가했습니다.
- 새로운 mame2003 코어 추가.
- 새로운 코어에 대한 디버그 엠스크립트 설정 지원이 추가되었습니다.

# 2.0.1 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/a72222c39a793c4ff470ebb2b71c04829fee4b5e)
- 베타 코어에 대한 제어 매핑.
- 베타 코어 업데이트.
- 이제 베타 코어가 기본 옵션입니다!
- a5200 코어 추가.
- 새로운 n6의 저장 상태 수정

# 1.1.6 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/fa153ba76791184d978f9fb8b69991b05b161bc8)
- 액시오스 모듈을 커스텀 스크립트로 대체했습니다.
- 베타 코어에 일시정지/재생 기능을 추가했습니다.
- CSS를 자체 파일로 분리.
- emu-min.js의 이름을 emulator.min.js로 변경.

# 1.1.5 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/2767c635b8a6e05c57e054d2f9d01ae0c4ff6d47)
- 페치 오류 함수를 정리했습니다.
- 가상 게임패드 이벤트 리스너를 정리했습니다.
- 행동 강령 추가.

# 1.1.2 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/64731dd8219931155b4e698aa98dbf65c2120038)
- mame 파일 이름이 잘못 지정되는 오류를 수정했습니다.
- loader.js에서 참조된 변수가 정의되지 않은 버그를 수정했습니다.
- .gitignore 추가
- js 파일을 축소하는 nodejs 스크립트를 추가했습니다.
- 화면 녹화에 오디오를 추가했습니다.
- emulator.js 파일에서 많은 죽은 코드를 제거했습니다.
- axios 모듈 업데이트.
- CORS 오류 메시지 추가
- nodejs 버퍼 모듈 업데이트.

# 1.1.0 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/715ded4ae23c2135bc9a8b9b7599f12c905393b3)
- 축소 기능이 추가되었습니다.
- 에뮬레이터js 로고 추가.
- 베타 ND 및 GB 코어를 추가했습니다.
- 이전 코어가 아닌 베타 코어에서 WASM이 지원될 때 베타를 사용하지 않을 경우 네트워크 오류가 표시되는 버그가 수정되었습니다.
- 베타 코어에 볼륨 설정 및 치트를 추가했습니다.

# 1.0 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/fde44b095bb89e299daaaa4c8d7deebc79019865)
- 베타 코어 공식 출시.
- 프로덕션에서 베타 코어를 사용할 수 있습니다.
- 이전 에뮬레이터js 넷플레이 서버를 사용할 수 있습니다.
- 화면 녹화 출력 파일 이름(있는 경우)을 게임명으로 설정합니다.
- 스크린샷이 있는 경우 파일 이름을 게임명으로 설정합니다.
- 함수가 배열로 참조되는 가상 게임패드 버그가 수정되었습니다.

# 0.4.26 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/0709829a11266b6ab4bbbf3e61d6dd6d3c372133)
- 에뮬레이터.js 파일을 2개의 파일로 분리했습니다.
- 사용자 지정 넷플레이 서버에 대한 지원이 추가되었습니다.
- 넷플레이 방 비밀번호 입력 버그를 수정했습니다.
- iOS에서 가상 게임패드 영역이 응답하지 않던 버그를 수정했습니다.
- 상태 위치 저장 기능을 추가했습니다.
- 마메 코어 설정이 추가되었습니다.
- 베타 코어를 추가했습니다!
- 현지화를 추가했습니다.
- 가상 게임패드 코드를 다시 작성했습니다.
- EJS_terminate 함수를 추가했습니다.
- 창에 simulate_input 함수를 노출했습니다.
- webrtc 어댑터를 업데이트했습니다.

# 0.4.25 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/ef3200ef87bffe57241e05ae9646cc201142ec46)
- 시작 시 로드 상태를 loader.js 파일에서 emulator.js 파일로 이동했습니다.
- 데이터 경로 함수를 loader.js 파일에서 emulator.js 파일로 옮겼습니다.
- EJS_pathtodata` 변수를 통해 데이터의 사용자 지정 경로를 설정하는 기능을 추가했습니다.
- 사용자 지정 경로에 대한 지원 추가.
- 모듈과 로더를 창에 노출합니다.
- 로드 시 에뮬레이터를 시작하기 위해 `EJS_startOnLoaded`를 추가했습니다.
- 빠른 저장 상태 슬롯을 추가했습니다.
- 저장 상태 메시지를 추가했습니다.
- 저장 상태가 지원되는 경우에만 설정에 저장 상태 슬롯을 표시합니다.
- DS 포인터 잠금을 추가했습니다.
- 가상 게임 패드에 메뉴 버튼을 추가했습니다. 메뉴는 모바일에서 클릭했을 때만 열립니다.
- 라이선스 생성
- 공식 에뮬레이터js 웹사이트 생성.

# 0.4.24 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/73ff641616bcd10f088a004002183760832a1afc)
- 에뮬레이터.js 및 로더.js 파일을 최대한 많이 제거했습니다.
- 빠른 저장/로드 단축키를 추가했습니다.
- 게임패드 축을 버튼으로 사용할 수 있는 기능을 추가했습니다.
- 컨트롤 제목의 오타를 수정했습니다.
- 컨트롤 설정에서 시스템별로 필요한 입력만 표시합니다.
- loader.js 파일을 다시 작성했습니다.
- 일부 변수를 창에 노출시켰습니다.
- 컨텍스트 메뉴 코드를 정리했습니다.
- emulator.js 파일에서 일부 구문을 정리했습니다.
- loader.js 파일을 통해 `EJS_AdUrl`을 선언했습니다.
- 축을 버튼으로 매핑해도 작동하지 않던 버그 수정.
- 누락된 레거시 n64 코어를 추가했습니다.
- n64 코어 업데이트.

# 0.4.23-07 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/83e148c82cbc8b4e835a808dcf84456975f82a7c)
- 불필요한 코드를 제거했습니다.
- 제어 설정에 재설정 버튼을 추가했습니다.
- 설정을 제어하기 위해 지우기 버튼을 추가했습니다.
- 에뮬레이터에 광고를 추가하는 기능인 `EJS_AdUrl` 옵션을 추가했습니다.
- 일부 파일 불러오기를 정리했습니다.
- RAR 압축 해제 수정.

# 0.4.23-05 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/018c787ccf6daca58c863d38fff61910f33f98ec)
- 더 이상 `파일:` 및 `chrome-extension:` 프로토콜을 사용하는 게임을 캐시하지 않습니다.
- 기본 키매핑을 변경했습니다.
- 화면 녹화 버튼을 추가했습니다.

# 0.4.23-04 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/6464bbedc1cd58c023cd66656540fc174aedde8b)
- mame2003, snes2002, snes2005, snes2010 및 vbanext 코어를 추가했습니다.
- 지원되는 모든 코어에 대해 asmjs를 추가했습니다.

# 0.4.23-03 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/c883f267e1e56ed6b6472b891f78704c6e4b4c17)
- loader.js 디옵스포큐팅을 시작합니다.
- extractzip.js 압축 해제.
- 저장 상태의 파일 이름을 변경하는 기능인 `EJS_gameName`을 추가했습니다.

# 0.4.23-02 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5d97620b25a81e49c6ba313e586fb37a5ce66002)
- Start emulator.js  deobsfocuting.

# 0.4.23-01 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/42a7e129cfded266b72539e8d1b5978d5e4119d8)
- “blob:” URL 로딩을 지원합니다.
- 게임 시작 시 로딩 상태 지원을 추가했습니다.

# 0.4.23 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/5f5cf5cbba29cfd772d525a4c73a4bc5ea26654c)
- 업데이트 가능 메시지를 추가했습니다.
- 게임 시작 시 광고 아이프레임의 'X'가 계속 표시되던 버그를 수정했습니다.
- a2600 및 마메 코어를 추가했습니다.
- 보이는 'x' 제거
- 압축 파일 추출 지원을 추가했습니다.

# 0.4.19 [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/4fd22871663e5896bb5d0ce29a50ad508462387a)
- 32X, 3도, A7800, 아케이드, 블루엠엑스, 재규어, 링스, NGP, PCE, 새턴, 세가, 세그아드 및 WS 코어에 대한 지원이 추가되었습니다.

# Initial release [트리 보기](https://github.com/EmulatorJS/EmulatorJS/tree/be2db16cba8bd85bf901cd89ca6de51414cea792)
- zip 파일 압축 해제 지원.
- 7zip 파일 압축 해제 지원.
- vb, snes, psx, nes, nds, n64, gba 및 gb 시스템 지원. WASM만 지원합니다.
