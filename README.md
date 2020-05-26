# 1. Iaas/PaaS/SaaS
#### 1) IaaS: Infrastructure as a Service
서버 운영을 위한 인프라 구축을 가상의 환경에서 편리하게 이용할 수 있게 서비스 형태로 제공
기존 서버 호스팅보다 하드웨어 확장성이 좋고, 탄력적이며 빠른 제공을 할 수 있는 가상화 기술 이용
클라이언트는 서비스 제공업체의 클라우드 환경에 구축하고 싶은 os와 응용프로그램을 성정하여 사용
물리적 자원 (서버, 네트워크, OS, 스토리지)을 가상화 하여 제공하고 관리
   #### 장점
   물리적 자원에 대한 관리를 논리적인 영역으로 대체할 수 있다
물리적 자원에 대한 자동화된 배포가 가능하다
물리적 자원에 댛ㄴ 안정적인 운영을 벤더에 맡길 수 있다
물리적 자원에 대한 규모의 확장 또는 축솨가 자유롭다
ex) Amazon EC2


#### 2) PaaS: Platform as a Service
서비스를 개발 할 수 있는 안정적인 환경과 그 환경을 이용하는 응용 프로그램을 개발할 수 있는 
API까지 제공하는 형태
앱의 개발 및 시작과 관련된 인프라를 만들고 유지보수 하는 복잡함 없이 고객이 어플리케이션을
개발, 실행, 관리할 수 있게 하는 플랫폼 제공 형태
소프트웨어 작성을 위한 플랫폼(OS, 미들웨어, 런타임)을 가상화하여 제공하고 관리
   #### 장점
   소프트웨어 유지 관리가 쉬워진다
가상화 기술을 기반으로 구축되어 비즈니스가 변함에 따라 리소스를 쉽게 확장, 축소 가능
응용 프로그램 개발, 테스트 및 배포를 지원하는 다양한 서비스 제공
수많은 사용자가 동일한 개발 응용 프로그램에 액세스 가능
   #### 단점
   특정 플랫폼 서비스에 종속될 수 있다.
ex) Google Cloud Platform, Naver Cloud Platform


#### 3) SaaS: Software as a Service
소프트웨어 및 관련 데이터는 중앙에 호스팅되고 사용자는 웹 브라우저 등의 클라이언트를 통해
접속하는 형태의 소프트웨어 전달 형태
클라우드 환경에서 동작하는 응용프로그램을 서비스 형태로 제공하는 것
웹 브라우저를 통해 직접 실행되므로 클라이언트 측에서 다운로드나 설치가 불필요
고객을 대신하여 소프트웨어와 데이터를 제공하고 관리
   #### 장점
   소프트웨어 설치, 관리 및 업그레이드와 같은 작업에 소요되는 시간과 비용을 줄임
소프트웨어를 설치할 물리적 자원 불필요
언제 어디서든 접근 가능
    #### 단점
커스터마이징이 어렵다
ex)MS office, Gmail