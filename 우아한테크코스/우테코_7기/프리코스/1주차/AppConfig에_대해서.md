# AppConfig

## AppConfig 설명

AppConfig 클래스는 Spring Framework에서 애플리케이션의 구성(configuration)을 관리하는 역할을 합니다.
이 클래스에서는 애플리케이션에서 사용할 다양한 Bean(객체)을 정의하고 설정합니다. 이 Bean들은 뷰(View), 
레포지토리(Repository), 서비스(Service), 컨트롤러(Controller) 계층 간의 의존성을 관리하는 데 사용됩니다.

## 구성 요소

### View:

사용자 인터페이스의 일부로, 사용자와 상호작용하는 컴포넌트를 포함합니다.
사용자 입력을 받고, 결과를 표시하는 역할을 합니다.
### Repository:

데이터에 대한 CRUD(Create, Read, Update, Delete) 작업을 담당합니다.
데이터베이스와의 상호작용을 통해 데이터를 가져오거나 저장하는 로직을 포함합니다.
MemorySeparatorRepository와 같은 클래스가 이 계층에 해당합니다.
### Service:

비즈니스 로직을 처리하는 계층입니다.
사용자 요청에 대한 처리를 담당하며, 필요한 경우 여러 레포지토리와 상호작용합니다.
SeparatorServiceImpl 클래스는 이 계층의 구현체로, 데이터 처리 및 변환을 수행합니다.
### Controller:

사용자 요청을 받고 응답을 반환하는 계층입니다.
HTTP 요청을 처리하고, 서비스 레이어와 상호작용하여 비즈니스 로직을 호출합니다.
SeparatorController와 같은 클래스가 이 계층에 해당합니다.
Bean 관리
### Dependency Injection:

AppConfig 클래스에서 정의한 Bean들은 서로 의존성을 가지고 있으며, Spring의 의존성 주입(Dependency Injection) 
기능을 통해 자동으로 주입됩니다.
예를 들어, SeparatorServiceImpl은 MemorySeparatorRepository에 의존하며, SeparatorController는 
SeparatorServiceImpl에 의존합니다.
### Bean의 생명주기 관리:

Spring은 각 Bean의 생명주기를 관리하며, 필요에 따라 생성 및 파괴됩니다. 이는 애플리케이션의 효율성과 유지보수성을 
높이는 데 기여합니다.
사용 목적
AppConfig 클래스의 주된 목적은 애플리케이션 구조를 명확하게 하고, 각 계층 간의 의존성을 쉽게 관리할 수 있도록 
하는 것입니다. 이를 통해 개발자는 코드를 보다 모듈화하여 유지보수성과 확장성을 높일 수 있습니다.