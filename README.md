# :tv: 영화정보 검색 & 추천 API 



## Description

* 최신 영화 정보, 현재 인기 영화 목록, 주변 영화관 위치 검색 API
* 주제 선정 배경
  * 관심있는 영화에 대한 정보와 그 외 정보들을 방대한 양의 정보더미 속에서 찾아야하는 번거로음에 초점을 맞춤
* 기능
  * 영화 검색: 원하는 영화에 대한 최신 정보 출력
  * 현재 인기 영화 추천
  * 현재 사용자 근처 영화관의 위치 



## Requirement

* Python 3 or higher
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
