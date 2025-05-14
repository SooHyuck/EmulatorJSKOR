
<div align = center>

<img width = 300 src = docs/Logo-light.png#gh-dark-mode-only>
<img width = 300 src = docs/Logo.png#gh-light-mode-only> 
 
<br>
<br>

[![Badge License]][License]
    
    
다양한 시스템을 위한 자체 호스팅 **Javascript** 에뮬레이션입니다.

<br>

[![Button Website]][Website]
[![Button Usage]][Usage]<br>
[![Button Configurator]][Configurator]<br>
[![Button Demo]][Demo]<br>
[![Button Contributors]][Contributors]

 
디스코드 서버에 참여하세요:

[![디스코드 서버에 참여하세요!](https://invidget.switchblade.xyz/6akryGkETU)](https://discord.gg/6akryGkETU)

또는 Matrix 서버(#emulatorjs:matrix.emulatorjs.org)를 사용하세요:

<a href="https://matrix.to/#/#emulatorjs:matrix.emulatorjs.org" rel="noopener" target="_blank"><img src="https://matrix.to/img/matrix-badge.svg" alt="매트릭스에서 채팅하기"></a>

</div>

<br>

> [!참고] 
> **EmulatorJS 버전 4.0부터 이 프로젝트는 더 이상 emulatorjs.com 프로젝트의 리버스 엔지니어링 버전이 아닙니다. 이제 완전히 다시 작성되었습니다.**

> [!경고] 
> 버전 4.0.9부터 코어 및 축소 파일은 더 이상 리포지토리에 포함되지 않습니다. 별도로 다운로드해야 합니다. 릴리즈](https://github.com/EmulatorJS/EmulatorJS/releases) 또는 * 새 CDN에서 받을 수 있습니다(자세한 내용은 [this](#CDN) 참조). 또한 새로운 버전 시스템을 사용할 예정입니다. (자세한 내용은 [여기](#버버링)를 참조하세요).
>
> 프로젝트의 히스토리가 다시 작성되어 강제 푸시되었습니다. 활성 커밋을 다시 실행해야 할 수도 있습니다. 불편을 드려 죄송합니다.

> [!팁] >
> 리포지토리 복제는 더 이상 프로덕션용으로 권장되지 않습니다. 대신 [릴리즈](https://github.com/EmulatorJS/EmulatorJS/releases) 또는 [CDN](https://cdn.emulatorjs.org/)을 사용해야 합니다.

<br>

### 광고

*이 프로젝트에는 광고가 없습니다.* <br>
*하지만 현재 데모 페이지에는 이 프로젝트의 펀딩을 돕기 위한 광고가 있습니다.* <br>
*데모 페이지의 광고는 사용자 수에 따라 나타났다 사라질 수 있습니다* <br>
*이 프로젝트에 펀딩하는 사람 수에 따라 광고가 표시될 수 있습니다.* <br>

***[patreon]***에서 이 프로젝트의 펀딩을 도울 수 있습니다.

<br>


### 이슈

*문제가 해결되지 않는 경우 ***[Issue]***를 개설해 주세요.
*콘솔 로그와 함께 가능한 한 많은 세부 정보를 알려주세요.

<br>

### 버전 관리
알아두셔야 할 세 가지 버전 이름이 있습니다:
1. **stable** - 출시 전에 코드와 코어가 모두 테스트되는 가장 안정적인 버전의 에뮬레이터입니다. 이 버전은 GitHub에 새 버전이 출시될 때마다 업데이트됩니다. 데모의 기본 버전입니다.
2. **latest** - 최신 코드를 포함하지만 안정적인 코어를 사용합니다. 메인 브랜치가 업데이트될 때마다 업데이트됩니다.
3. **nightly** - 최신 코드와 최신 코어를 포함합니다. 코어는 매일 업데이트되므로 계속 알파로 업데이트됩니다.

### CDN
모든 버전의 에뮬레이터를 다운로드하는 데 사용할 수 있는 새로운 CDN이 있습니다. CDN은 `https://cdn.emulatorjs.org/`입니다. 이를 사용하여 `EJS_pathtodata`를 `https://cdn.emulatorjs.org/<버전>/data/`로 설정하여 안정적인 최신 버전, 야간 버전 및 기타 주요 버전을 얻을 수 있습니다.

### 확장 프로그램

 **[게임 라이브러리]**

   ***ROM** 폴더에 대한 라이브러리 개요입니다.*

<br>

### 개발:

*다음 명령어로 로컬 서버를 실행합니다. *
```
npm i
npm start
```

<br>

**>> 버그를 보고할 때는 이전 버전을 사용 중임을 명시하세요**.

<br>
<br>
<br>

<h1 align = center>지원되는 시스템</h1>

<br>

<div align = center>

### 닌텐도

**[게임보이 어드밴스][닌텐도 게임보이 어드밴스]** | 
**[패미컴 / NES][NES / 패미컴]** | 
**[버추얼 보이][버추얼 보이]**
    
**[게임보이][닌텐도 게임보이]** | 
**[슈퍼 패미컴 (SNES)]** | 
**[DS][닌텐도 DS]** | 
**[64][닌텐도 64]**

<br>
<br>

### 세가

**[마스터 시스템][세가 마스터 시스템]** | 
**[메가 드라이브][세가 메가 드라이브]** | 
**[게임 기어][세가 게임 기어]**
    
**[새턴][세가 새턴]** | 
**[32X][세가 32X]** | 
**[CD][세가 CD]**
    
<br>
<br>

### 아타리

**[2600][Atari 2600]** | 
**[5200][아타리 5200]** | 
**[7800][아타리 7800]** | 
**[Lynx][아타리 스라소니]** | 
**[재규어][아타리 재규어]**

<br>
<br>

### Commodore

**[Commodore 64]** |
**[Commodore 128]** |
**[Commodore Amiga]**

**[Commodore PET]** |
**[Commodore Plus/4]** |
**[Commodore VIC-20]**

<br>
<br>

### 기타
    
**[플레이스테이션]** | 
**[아케이드]** | 
**[3DO]**

**[마메 2003]** |
**[콜코비전]**
    
</div>

<br>

## 스타 히스토리

<a href="https://star-history.com/#EmulatorJS/EmulatorJS&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=EmulatorJS/EmulatorJS&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=EmulatorJS/EmulatorJS&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=EmulatorJS/EmulatorJS&type=Date" />
 </picture>
</a>

<!-- 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 --->

[License]: 라이센스
[Issue]: https://github.com/ethanaobrien/emulatorjs/issues
[patreon]: https://patreon.com/EmulatorJS


<!-- 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮   Extensions   🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 --->

[GameLibrary]: https://github.com/Ramaerel/emulatorjs-GameLibrary


<!-- 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮   Quicklinks   🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 --->

[Configurator]: https://emulatorjs.org/editor
[Contributors]: docs/Contributors.md
[Website]: https://emulatorjs.org/
[Usage]: https://emulatorjs.org/docs/
[Demo]: https://demo.emulatorjs.org/


<!-- 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮  Systems  🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 -->

[Nintendo Game Boy Advance]: https://emulatorjs.org/docs/systems/nintendo-game-boy-advance
[Nintendo Game Boy]: https://emulatorjs.org/docs/systems/nintendo-game-boy
[Nintendo 64]: https://emulatorjs.org/docs/systems/nintendo-64
[Nintendo DS]: https://emulatorjs.org/docs/systems/nintendo-ds

[Sega Master System]: https://emulatorjs.org/docs/systems/sega-master-system
[Sega Mega Drive]: https://emulatorjs.org/docs/systems/sega-mega-drive
[Sega Game Gear]: https://emulatorjs.org/docs/systems/sega-game-gear
[Sega Saturn]: https://emulatorjs.org/docs/systems/sega-saturn
[Sega 32X]: https://emulatorjs.org/docs/systems/sega-32x
[Sega CD]: https://emulatorjs.org/docs/systems/sega-cd

[Atari Jaguar]: https://emulatorjs.org/docs/systems/atari-jaguar
[Atari Lynx]: https://emulatorjs.org/docs/systems/atari-lynx
[Atari 7800]: https://emulatorjs.org/docs/systems/atari-7800
[Atari 2600]: https://emulatorjs.org/docs/systems/atari-2600
[Atari 5200]: https://emulatorjs.org/docs/systems/atari-5200

[NES / Famicom]: https://emulatorjs.org/docs/systems/nes-famicom
[SNES]: https://emulatorjs.org/docs/systems/snes

<!--
[TurboGrafs-16 / PC Engine]: https://emulatorjs.org/systems/TurboGrafx-16
[MSX]: https://emulatorjs.org/systems/MSX
[WanderSwan / Color]: https://emulatorjs.org/systems/WonderSwan
[Neo Geo Poket]: https://emulatorjs.org/systems/Neo%20Geo%20Pocket
--->
[PlayStation]: https://emulatorjs.org/docs/systems/playstation
[Virtual Boy]: https://emulatorjs.org/docs/systems/virtual-boy
[Arcade]: https://emulatorjs.org/docs/systems/arcade
[3DO]: https://emulatorjs.org/docs/systems/3do
[MAME 2003]: https://emulatorjs.org/docs/systems/mame-2003
[ColecoVision]: https://emulatorjs.org/docs/systems/colecovision

[Commodore 64]: https://emulatorjs.org/docs/systems/commodore-64
[Commodore 128]: https://emulatorjs.org/docs/systems/commodore-128
[Commodore Amiga]: https://emulatorjs.org/docs/systems/commodore-amiga
[Commodore PET]: https://emulatorjs.org/docs/systems/commodore-pet
[Commodore Plus/4]: https://emulatorjs.org/docs/systems/commodore-plus4
[Commodore VIC-20]: https://emulatorjs.org/docs/systems/commodore-vic20


<!-- 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮  Badges  🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 🎮 --->

[Badge License]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge

[Button Configurator]: https://img.shields.io/badge/Configurator-992cb3?style=for-the-badge
[Button Contributors]: https://img.shields.io/badge/Contributors-54b7dd?style=for-the-badge
[Button Website]: https://img.shields.io/badge/Website-736e9b?style=for-the-badge
[Button Usage]: https://img.shields.io/badge/Usage-2478b5?style=for-the-badge
[Button Demo]: https://img.shields.io/badge/Demo-528116?style=for-the-badge
[Button Beta]: https://img.shields.io/badge/Beta-bb044f?style=for-the-badge
