# Self-Driving-Car-Cone-Keeping-Assistance-System 🚗

이 레포지토리는 콘을 가상 차선으로 인식하고 이를 이용해 차선유지 자율주행 보조 시스템을 구축하는 프로젝트입니다.

---

## 📚 프로젝트 개요

이 프로젝트는 2023 대학생 창작 모빌리티 경진대회의 자율주행 성능 부문에 참가하기 위해 개발되었습니다. 작년에 참여한 국제 창작 자동차 경진대회 전기차부문 자율주행 파트의 코드는 '22_LKAS' 폴더에 업로드 되어 있습니다. 이번 대회를 위한 새로운 코드는 레포지토리에 곧 업로드 될 예정입니다.

---

## 👥 팀 구성

- **총괄 팀장**: 김서현

### 인지 - 비전
- 파트장: 김다현
- 파트원: 이동주, 서형찬, 이동국

### 인지 - 라이다
- 파트장: 황석환
- 파트원: 이현승, 김대완, 김지일, 박정빈, 이찬영, 현덕

### 판단
- 파트장: 김재혁
- 파트원: 이효민, 박정은, 우수한, 김대완, 이현승, 이동주, 김다현

### 제어
- 파트장: 윤다빈
- 파트원: 김민우, 서우진, 이동국, 이찬영, 황석환, 민채원

### 배선
- 파트장: 민채원
- 파트원: 황민기, 서우진, 이동국, 이찬영, 윤다빈

---

## 🏆 대회 정보

- 대회명: 2023 대학생 창작 모빌리티 경진대회
- 주최: 국토교통부
- 주관: 한국교통안전공단, (사)한국자동차안전학회
- 참가 부문: 자율주행 성능 부문

작년에 우리 팀은 국제 창작 자동차 경진대회 전기차부문 자율주행 파트에서 참가했으며, 상위 2개팀에게 부여하는 특별상을 수상했습니다. 작년 대회에 대한 자세한 내용은 '22_LKAS' 폴더를 참조하시기 바랍니다.

<img src="https://github.com/Deep-of-Machine/Self-Driving-Car-Cone-Keeping-Assistance-System/assets/90141741/cd593be4-ebb5-42f4-b0af-a06efa4a6ad3" width="600" height="400">




---

## 🚀 2023 대회 미션

올해 대회미션은 다음과 같습니다. 모든 미션은 무인 자율주행으로 이루어집니다.

---

### 1️⃣ 제동 검사

자동차가 40km/h 이상의 속도에서 제동 시 제동한계선 (6m) 이내에 안전하게 제동할 수 있는지 평가합니다. 세부적으로는 첫번째로 원격 제동 검사로 E-Stop 제동 리모컨으로 정지합니다. 두번째로는 제동 구역 끝에 있는 콘을 라이다 또는 카메라를 이용하여 인식하여 정지합니다.

![image](https://github.com/Deep-of-Machine/Self-Driving-Car-Cone-Keeping-Assistance-System/assets/90141741/f896bb15-6b7d-4b8f-b831-4e02c9adb411)

---

### 2️⃣ 가속 성능

경기장에서 출발신호와 함께 출발하여 가속하며, 자율주행 상태에서 5m 폭의 직진 차선을 따라 150m 길이의 경기 코스를 가능한 빠른 시간 내에 완주하는 것입니다.

![image](https://github.com/Deep-of-Machine/Self-Driving-Car-Cone-Keeping-Assistance-System/assets/90141741/57ae2f71-58eb-447e-bc5c-613d820a75e5)


---

### 3️⃣ 조향 성능

S자 곡선 차선 모양의 경기장에서 출발신호와 함께 장애물을 피하면서 지정된 경로를 주행하여 도착할 때 까지의 추돌한 콘의 개수를 측정합니다.

![image](https://github.com/Deep-of-Machine/Self-Driving-Car-Cone-Keeping-Assistance-System/assets/90141741/61a9e96e-35a1-4811-99d7-24a1ee496b9a)

---

### 4️⃣ 종합주행성능

종합 주행 성능 미션은 자율주행 상태에서 250m/lap 포장도로 주행 코스를 2바퀴 총 500m를 반 시계방향으로 주행하는 것입니다.

<img src="https://github.com/Deep-of-Machine/Self-Driving-Car-Cone-Keeping-Assistance-System/assets/90141741/cc7c8a31-594d-4efb-b167-c4c9077b8bce" width="600" height="400">


---

이 외에도 안전을 위한 ASMS(Autonomous System Master Switch), 가상엔진음 발생시스템(Virtual Engine Sound System), LED 주행 상태 표시 등이 필요합니다.
