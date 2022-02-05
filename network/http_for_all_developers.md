# 모든 개발자를 위한 HTTP 웹 기본 지식

> 본 문서는 [모든 개발자를 위한 HTTP 웹 기본 지식](https://www.inflearn.com/course/http-웹-네트워크) 강의를 보고 제 주관대로 정리한 글입니다.

---

# 인터넷 네트워크

> 인터넷에서 컴퓨터들은 어떻게 통신할까?

## IP(Internet Protocol) - 인터넷 프로토콜

### IP의 역할

- 지정한 **_IP 주소_**(IP Address)에 데이터를 전달한다.
- 데이터를 전달할 때는 **_패킷_**(Packet)이라는 통신 단위를 사용하는데 다음과 같은 정보를 포함한다.
  - 출발지 IP 주소
  - 목적지 IP 주소
  - 전달할 데이터, 기타 등
- 패킷(Packet)은 패키지(Package)와 버킷(Bucket)의 합성어

### IP의 한계

- 비연결성: 대상 서버가 패킷을 받을 수 있는 상황인지 모르기 때문에 패킷을 받을 대상이 없거나 서비스 불능 상태여도 패킷을 전송한다.
- 비신뢰성: 중간에 패킷이 사라지거나 패킷이 순서대로 도착하지 않을 수 있다.
- 프로그램 구분: 같은 IP 주소를 사용하는 서버에서 통신하는 프로그램이 여러 개일 경우 구분할 필요가 있다.

## TCP(Transmission Control Protocol) - 전송 제어 프로토콜

> 신뢰할 수 있는 프로토콜

### TCP 특징

- 연결 지향적 - 3 Way Handshake (가상 연결: 논리적으로만 연결한다)
- 데이터 전달 보증 - 클라이언트가 데이터를 보내면, 서버가 데이터를 받았다는 응답을 보냄으로써 데이터가 잘 전달됐는지 확인한다.
- 순서 보장 - 클라이언트가 패킷 1, 2, 3을 순서대로 보냈을 때, 서버가 1, 3, 2 순서로 패킷을 받았다면 2부터 다시 패킷을 보내라고 요청한다.
- 현재는 대부분 TCP 사용
- TCP는 **_세그먼트_**(Segment)라는 단위로 데이터를 전달하며 다음과 같은 정보를 포함한다.
  - 출발지 포트
  - 목적지 포트
  - 전송 제어 정보
  - 순서 정보
  - 검증 정보
  - 전달할 데이터, 기타 등

### TCP 3 Way Handshake

1. 클라이언트가 서버한테 SYN(Synchronize)라는 접속 요청 메세지를 보낸다.
2. 클라이언트의 SYN 메세지를 받은 서버는 ACK(Acknowledgment)라는 요청 수락 메세지와 함께 SYN 메세지를 다시 클라이언트한테 보낸다.
3. 서버의 SYN + ACK 메세지를 받은 클라이언트가 다시 ACK 메세지를 보내고 서버에 도착하면 비로소 연결이 완료된다.
4. 이후엔 데이터를 주고 받을 수 있으며, 3번의 ACK 메세지와 함께 데이터를 보내는 것도 가능하다.

## UDP(User Datagram Protocol) - 사용자 데이터그램 프로토콜

> 기능이 거의 없어 화얀 도야지에 비유된다.

### UDP 특징

- 연결 지향 X
- 데이터 전달 보증 X
- 순서 보장 X
- 포트(Port)와 체크섬(Checksum) 정도만 추가

### UDP를 왜 쓸까?

- 기능이 적은 만큼 단순하고 빠르다.
- 어플리케이션 수준에서 커스텀 하기 용이하다.
- HTTP/3에서 TCP 대신 UDP 기반으로 구글이 개발한 QUIC을 사용한다.

## 포트(Port)

> 같은 IP 내에서 프로세스를 구분한다.

- IP 주소가 아파트라면, 포트는 호수에 비유할 수 있다.
  - E.g., OO 아파트 103동은 IP 주소, 401호는 포트
- 컴퓨터로 게임, 화상 통화, 웹 브라우저 요청 등 여러 작업을 한 번에 하고 있다면 어떻게 구분할 것인가? 포트로 구분한다.
- 서버에 요청을 할 때, TCP/IP 패킷에 출발지 포트도 같이 보내기 때문에 서버에서 응답할 때도 내가 요청한 포트로 응답을 보낸다.
- 포트는 0부터 65535까지 할당할 수 있다.
- 0부터 1023은 잘 알려진 포트(Well-known Port)로 겹칠 수 있기 때문에 사용하지 않는 것이 좋다.
  - FTP - 20, 21
  - TELNET - 23
  - HTTP - 80
  - HTTPS - 443

## DNS(Domain Name System) - 도메인 네임 시스템

### DNS를 쓰는 이유

- IP 주소는 외우기 어렵다.
- IP 주소는 변경될 수 있다.

### DNS의 역할

- 인터넷 세상에서 전화번호부 같은 역할을 한다.
- 도메인 이름을 IP 주소로 변환한다.

### DNS 동작 방식

| 도메인 이름 |    IP 주소    |
| :---------: | :-----------: |
| google.com  | 200.200.200.2 |
|   aaa.com   | 210.210.210.3 |

- DNS 서버는 위와 같이 도메인 서버와 IP 주소가 매핑되는 테이블을 갖고 있다.
- 클라이언트가 *google.com*이란 도메인 이름에 해당하는 IP 주소를 찾아달라고 요청하면 *200.200.200.2*를 응답한다.

# URI와 웹 브라우저 요청 흐름

## URI(Uniform Resource Identifier)

### UR**I**? UR**L**? UR**N**?

- "URI는 로케이터(**L**ocator), 이름(**N**ame) 또는 둘다 추가로 분류될 수 있다.
  - [https://www.ietf.org/rfc/rfc3986.txt](https://www.ietf.org/rfc/rfc3986.txt) - 1.1.3. URI, URL, and URN
- URI는 URL과 URN을 포함하는 개념이라 할 수 있다.

### URI

- Uniform: 리소스를 식별하는 통일된 방식
- Resource: 자원, URI로 식별할 수 있는 모든 것
- Identifier: 다른 항목과 구분하는 데 필요한 정보

### URL, URN

- URL - Locator: 리소스가 있는 위치를 지정한다.
- URN - Name: 리소스에 이름을 부여한다.
- 위치는 변할 수 있지만, 이름은 변하지 않는다.
- URN의 예시, urn:isgn:8960777331
- URN만으로 실제 리소스를 찾는 방법은 보편화 돼 있지 않아서 주로 URL을 사용한다.

### URL 분석

```
scheme://[userinfo@]host[:port][/path][?query][#fragment]
https://www.google.com/search?q=hello&hl=ko`
```

- 요약
  - 스키마(프로토콜): https
  - 호스트: wwww.google.com
  - 포트: 443
  - 패스: /search
  - 쿼리 파라미터: q=hello&hl=ko
- scheme
  - 주로 프로토콜을 사용한다.
  - 프로토콜은 어떤 방식으로 자원에 접근할 것인가 하는 약속
    - E.g., https, https, ftp, etc.
- userinfo
  - URL에 사용자 정보를 포함해서 인증
  - 거의 사용하지 않음
- host
  - 호스트명: 도메인명 또는 IP 주소 직접 사용 가능
- port
  - 일반적으로 생략, 생략시 http는 80, https는 443
- path
  - 리소스 경로, 계층적 구조
  - E.g.
    - /home/file1.jpg
    - /members
    - /members/100, /items/iphone12
- query
  - key=value 형태
  - ?로 시작하고, &로 추가 가능
    - E.g., ?keyA=valueA&keyB=valueB
  - query parameter, query string 등으로도 부름
- fragment
  - html 내부 북마크 등에 사용
  - 서버로 전송되는 정보는 아님

## 웹 브라우저 요청 흐름

웹 브라우저가 `https://www.google.com/search?q=hello&hl=ko`로 요청을 보낸다 가정

- `www.google.com`의 실제 IP 주소를 DNS를 통해 조회한다.
- 포트 번호는 생략됐지만 https이기 때문에 기본적으로 443을 가진다.
- 다음과 같은 HTTP 요청 메세지를 만든다.

```
GET /search?q=hello&hl=ko HTTP/1.1
Host: www.google.com
```

- 웹 브라우저가 생성한 HTTP 메시지를 여러 계층을 통해 TCP/IP 패킷으로 감싼 후, 인터넷을 통해 서버로 보낸다.
- 요청을 받은 서버는 다음과 같이 그에 맞는 응답 메시지를 만들어 다시 클라이언트(웹 브라우저)로 보낸다.

```
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 3423
<html>
 <body>...</body>
</html>
```

- 서버의 응답을 받은 웹 브라우저는 메시지를 분석해 HTML을 렌더링한다.

# HTTP 기본

> **H**yper**T**ext **T**ransfer **P**rotocol

## 모든 것이 HTTP

- HTML 문서나 텍스트 뿐만 아니라 이미지, 음성, 영상 등의 파일, API에 주로 쓰이는 JSON, XML까지 거의 모든 형태의 데이터 전송이 가능
- 서버 간에 데이터를 주고 받을 때도 대부분 HTTP를 사용

### HTTP 역사

- HTTP/0.9 1991년: GET 메서드만 지원, HTTP 헤더X
- HTTP/1.0 1996년: 메서드, 헤더 추가
- HTTP/1.1 1997년: **가장 많이 사용, 우리에게 가장 중요한 버전**
  - RFC2068 (1997) -> RFC2616 (1999) -> RFC7230~7235 (2014)
- HTTP/2 2015년: 성능 개선
- HTTP/3 진행중: TCP 대신에 UDP 사용, 성능 개선

### 기반 프로토콜

- TCP: HTTP/1.1, HTTP/2
- UDP: HTTP/3
- 2022년 2월 기준, 네이버 웨일 브라우저로 몇몇 사이트를 확인해본 바, 대부분 HTTP/2를 주로 사용했으며, 유튜브의 경우 HTTP/3을 주로 사용했다.

### HTTP 특징

- 클라이언트 서버 구조
- 무상태 프로토콜(Stateless), 비연결성
- 단순하고, 확장 가능하다.

## 클라이언트 서버 구조

- 클라이언트가 먼저 요청을 보내면, 그에 맞게 서버가 응답을 하는 구조다.
- 클라이언트와 서버를 분리함으로써 각각 독립적으로 진화할 수 있다는 장점이 있다.

## 무상태(Stateless) 프로토콜

- 서버가 클라이언트의 상태를 보존하지 않는다.
- 장점: 스케일 아웃이 쉽다.
- 단점: 클라이언트가 추가 데이터를 전송해야 한다.

### 상태 유지(Stateful)

- 어떤 가게에서 물건을 구매한다고 했을 때, 점원이 고객의 정보를 기억하고 있기 때문에 한 번 말했던 것은 계속 말할 필요가 없다.
- 중간에 점원이 바뀌면 안 된다.
  - 바뀐다면 고객에 대한 정보를 다른 점원에서 모두 알려줘야 한다.

### 무상태(Stateless)

- 어떤 가게에서 물건을 구매한다고 했을 때, 점원은 고객의 정보를 기억하지 않기 때문에 고객이 자신의 정보를 지속적으로 점원에게 말해줘야 한다.
- 중간에 점원이 바뀌어도 된다.
- 응답 서버를 쉽게 바꿀 수 있기 때문에 스케일 아웃에 유리하다.

### 실무에서 무상태(Stateless)의 한계

- 모든 것을 무상태로 설계하기엔 어려움이 있다.
  - E.g., 로그인
  - 로그인한 사용자의 경우, 로그인했다는 상태를 서버에 유지
  - 일반적으로 브라우저 쿠키와 서버 세션 등을 사용
- 상태 유지는 필요한 부분에만 최소한으로 사용하는 것이 좋다.

## 비연결성(Connectionless)

### 연결을 유지하는 모델

- 서버 한 대와 클라이언트 1, 2, 3이 있을 때, 이전에 클라이언트 1의 요청이 있었다면, 이후에 클라이언트 3과 통신할 때도 클라이언트 1과의 연결을 유지한다.

### 연결을 유지하지 않는 모델

- 서버 한 대와 클라이언트 1, 2, 3이 있을 때, 클라이언트 1의 요청에 대한 응답이 끝나면 바로 연결을 끊기 때문에 다른 클라이언트와 통신할 때는 클라이언트 1과의 연결 상태를 유지하지 않는다.

### 비연결성 특징

- HTTP는 기본적으로 연결을 유지하지 않는 모델
- 일반적으로 초 단위 이하의 빠른 속도로 응답
- 서버 자원을 매우 효율적으로 사용 가능

### 비연결성 한계와 극복

- 매번 TCP/IP 연결(e.g. 3 Way Handshake)을 새로 맺어야 하기 때문에 오버헤드가 증가한다.
- 웹 브라우저로 사이트를 요청할 때, HTML 뿐만 아니라 JS, CSS, 이미지 등 여러 리소스를 다운받는데 매번 새로 연결하면 매우 비효율적이다.
- 현재는 **HTTP 지속 연결**(Persistent Connections)로 문제를 해결했으며, HTTP/2와 HTTP/3에서 더욱 최적화됐다.

### HTTP 지속 연결(Persistent Connections)

- 클라이언트와 서버가 연결을 할 때 1초, 데이터를 주고 받을 때 1초, 연결을 종료할 때 1초가 걸린다고 가정한다.
- 지속 연결을 하지 않을 시, 3개의 데이터를 주고 받는다면 각각 연결과 종료를 하기 때문에 3초씩 총 9초가 걸린다.
- 지속 연결을 하면, 주고 받을 데이터가 있는 동안은 연결을 유지하기 때문에 연결 1초, 3개의 데이터 3초, 종료 1초, 총 5초가 걸린다.

## HTTP 메시지

![HTTP Message](images/http_message.png)

```
HTTP-message  = start-line
                *( header-filed CRLF )
                CRLF
                [ message- body ]
```

[공식 스펙](https://datatracker.ietf.org/doc/html/rfc7230#section-3)

### 시작 라인

#### 요청 메시지

```
GET /search?q=hello&hl=ko HTTP/1.1
```

- request-line = method SP(공백) request-target SP HTTP-version CRLF(엔터)
- HTTP 메서드: 서버가 수행해야 할 동작 - Get
- 요청 대상: 일반적으로 "/"로 시작하는 절대 경로 - /search?q=hello&hl=ko
- HTTP Version - HTTP/1.1

#### 응답 메시지

```
HTTP/1.1 200 OK
```

- status-line = HTTP-version SP status-code SP reason-phrase CRLF
- HTTP Version - HTTP/1.1
- 상태 코드: 요청 성공, 실패를 나타냄 - 200
- 이유 문구: 사람이 이해할 수 있는 짧은 상태 코드나 설명 - OK

### HTTP 헤더

#### 요청 메시지

```
Host: www.google.com
```

#### 응답 메시지

```
Content-Type: text/html;charset=UTF-8
Content-Length: 3423
```

- header-field = field-name ":" OWS(띄어쓰기 허용) field-value OWS
- field-name은 대소문자 구분 없음
- HTTP 전송에 필요한 모든 메타 데이터

### HTTP 메시지 바디

```
<html>
  <body>...</body>
</html>
```

- 실제 전송할 데이터
- HTML, 텍스트, 이미지, 영상, JSON 등 바이트로 표현할 수 있는 모든 데이터 전송 가능
