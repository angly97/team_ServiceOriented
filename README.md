# :tv: 영화정보 검색 & 추천 API 



## Description

* 최신 영화 정보, 현재 인기 영화 목록, 주변 영화관 위치 검색 API
* 주제 선정 배경
  * 관심있는 영화에 대한 정보와 그 외 정보들을 방대한 양의 정보더미 속에서 찾아야하는 번거로음에 초점을 맞춤
* 기능
  * 영화 검색: 원하는 영화에 대한 최신 정보 출력
  * 현재 인기 영화 추천
  * 현재 사용자 근처 영화관의 위치 
* 개발프레임워크
  * Flask
    * 선택한 이유
      * HTML, CSS, JS, Python같은 기초 지식이 있으면 쉽게 개발할 수 있음
      * 가볍게 사용 가능
        *  사용이 가벼움. 즉 코드 몇 줄이면 금방 서버를 만들 수 있음 (Django의 10%)
        *  자체적으로 제공하는 기능이 적어서 유연함
        *  가볍게 배포 가능


## Requirement

* Python 2.7 or higher
* flask



## Setup

```bash
# Install dependencies
$ pip install -r ./requirements.txt –user
```



### Test

```bash
# run server
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```



## API Document

* 영화 검색

  * 요청

    * URL

      |    API    | 메서드 |                    요청 URL                     | 출력 포맷 |
      | :-------: | :----: | :---------------------------------------------: | :-------: |
      | 영화 검색 |  GET   | http://15.165.160.58:5000/moviesearch/movieinfo |   JSON    |

    * Parameter

      |  Name   | Required | Type |                         Description                          |
      | :-----: | :------: | :--: | :----------------------------------------------------------: |
      |   key   |    Y     | str  |               발급받은 인증 키 값을 입력한다.                |
      | movieNm |    Y     | str  |               조회하고자 영화 제목을 입력한다.               |
      | listNum |    N     | str  | 출력되는 영화 제목 row 개수를 지정한다.<br />영화 검색 결과가 10개 이하일 때는 결과 개수만큼 출력한다. (default: "10",  최대: "10") |

  * 응답

    |   Name    | Type |       Description       |
    | :-------: | :--: | :---------------------: |
    | companyCd | str  | 제작사 코드를 출력한다. |
    | companyNm | str  |  제작사명을 출력한다.   |
    | peopleNm  | str  | 영화감독명을 출력한다.  |
    | genreAlt  | str  |  영화장르를 출력한다.   |
    |  movieNm  | str  |   영화명을 출력한다.    |
    | nationAlt | str  |  제작국가를 출력한다.   |
    |  openDt   | str  |  개봉연도를 출력한다.   |

    

* 현재 위치 주변 영화관 및 박스오피스 검색 기능

  * 요청

    * URL

      |                        API                         | 메서드 |                    요청 URL                    | 출력 포맷 |
      | :------------------------------------------------: | :----: | :--------------------------------------------: | :-------: |
      | 현재 위치 주변 영화관 및<br />박스오피스 검색 기능 |  GET   | http://15.165.160.58:5000/moviesearch/cineinfo |   JSON    |

    * Parameter

      |  Name   | Required | Type |                         Description                          |
      | :-----: | :------: | :--: | :----------------------------------------------------------: |
      |   key   |    Y     | str  |               발급받은 인증 키 값을 입력한다.                |
      |   ip    |    Y     | str  |            위치 정보를 위한 사용자 ip를 입력한다.            |
      | listNum |    N     | str  | 출력되는 영화관 row 개수를 지정한다.<br />. (default: "15",  최대: "15") |

  * 응답

    |     Name     | Type |                         Description                          |
    | :----------: | :--: | :----------------------------------------------------------: |
    |   audiAcc    | str  |                    누적관객수를 출력한다.                    |
    |   movieNm    | str  |                      영화명을 출력한다.                      |
    |    openDt    | str  |                   영화 개봉일을 출력한다.                    |
    |     rank     | str  |              전날의 박스오피스 순위를 출력한다.              |
    | address_name | str  |                  전체 지번 주소를 출력한다.                  |
    |   distance   | str  | 중심좌표까지의 거리를 출력한다.단, x, y 파라미터를 준 경우에만 존재한다.(단위 : meter) |
    |    phone     | str  |                 영화관 전화번호를 출력한다.                  |
    |  place_name  | str  |                     영화관명을 출력한다.                     |
    |  place_url   | str  |              영화관 상세페이지 url를 출력한다.               |
    

## Flask
 * Micro Web Framwork
   * Micro
     * 가벼운 기능 제공
     * 확장성 넓음
   * Framwork
     * 개발하는 프로젝트 구조, 라이브러리 모음 등 제공하는 개발 틀
   * 간단한 웹 사이트/API 서버 만드는 데 특화된 파이썬 웹 프레임워크
 * WSGI 프레임워크
 * 요새는 클라우딩 컴퓨팅의 발달로 Docker, Kubernetes와 접목하여, 소규모 컨테이너 단위로 기능 개발 후, 한 번에 배포하는 방식 자주 사용
 * 파이썬 인터프리터로 실행
   * 실행이 빠르게 됨 ?
 * MVC 패턴
   * Model  = DB
   * View = HTML
   * Control = \_\_init__.py의 라우터 함수들
 * 장점
   * 가볍게 배울 수 있음(Python, HTML/CSS, Javascrip 만 배우면 가능)
   * 가볍게 사용 가능
     * 코드 몇 줄이면 금방 만듦
     * Django 코드의 10%인 프레임워크
   * 가볍게 배포 가능
     *  virtualenv에 Flask 깔고 바로 배포 하면 됨
 * 단점
   * Django보다 자유도가 높아서 제공기능 적음
   * 복잡한 애플리케이션 개발 시, 해야할 것 많음 
