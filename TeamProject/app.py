from flask import Flask, make_response
from flask_restful import Resource, reqparse, Api
import urllib.request
import setting
import json
import datetime
import requests
from urllib.request import urlopen

app = Flask(__name__)
"""
@app.route('/', methods=['GET'])
def home():
    return '<h1>Movie Search API</h1><p>A prototype API for searching the movie and finding the cinema</p>'
"""

class movieInfo(Resource):
    def get(self):
        try:

            kobis_key = setting.kobis_api_key()

            # kobis - list

            parser = reqparse.RequestParser()
            parser.add_argument('movieNm', required=True, type=str, help='movieNm cannot be blank')
            parser.add_argument('listNum', required=False, type=str, help='listNum can be blank')
            args = parser.parse_args()

            movieNm = urllib.parse.quote(args['movieNm'])
            listNum = ""

            if args['listNum'] != None:
                listNum = urllib.parse.quote(args['listNum'])

            else:
                listNum = "10"

            list_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?itemPerPage=" + listNum + "&key=" + kobis_key + "&movieNm=" + movieNm

            res = urllib.request.Request(list_url)

            response = urllib.request.urlopen(res)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = response.read()
                movielist = response_body.decode('utf-8')

                list_data = json.loads(movielist)

                for i in list_data["movieListResult"]["movieList"]:
                    del i["movieCd"], i["movieNmEn"], i["prdtStatNm"], i["prdtYear"], i["repGenreNm"], i["typeNm"]


                json_result = json.dumps(list_data, ensure_ascii=False, indent=4, sort_keys=True)

                result = make_response(json_result)

            return result

        except Exception as e:
            return {'error': str(e)}


class cineInfo(Resource):
    def get(self):
        try:
            kobis_key = setting.kobis_api_key()
            kakao_key = setting.kakao_api_key()

            places_detail = {
                '서울': '0105001',
                '경기': '0105002',
                '강원': '0105003',
                '충북': '0105004',
                '충남': '0105005',
                '경북': '0105006',
                '경남': '0105007',
                '전북': '0105008',
                '전남': '0105009',
                '제주특별자치도': '0105010',
                '부산': '0105011',
                '대구': '0105012',
                '대전': '0105013',
                '울산': '0105014',
                '인천': '0105015',
                '광주': '0105016',
                '세종특별자치시': '0105017'
            }

            # cinema position
            lat = 0.0
            lon = 0.0

            parser = reqparse.RequestParser()
            parser.add_argument('ip', required=True, type=str, help='ip cannot be blank')
            parser.add_argument('listNum', required=False, type=int, help='listNum can be blank')
            args = parser.parse_args()

            if(args['listNum'] == None):
                args['listNum'] = 15
            query_request = "https://geolocation-db.com/json/%s" % args['ip']

            with urlopen(query_request) as url:
                data = json.loads(url.read().decode())
                # print(data)
                lat = float(data["latitude"])
                lon = float(data["longitude"])

            searching = '영화관'
            url = 'https://dapi.kakao.com/v2/local/search/keyword.json?y=' + str(lat) + '&x=' + str(
                lon) +'&size='+str(args['listNum']) +'&radius=20000&query={}'.format(searching)
            headers = {
                "Authorization": kakao_key
            }
            places = requests.get(url, headers=headers).json()['documents']

            place_list = []
            for i in places:
                i['distance'] = int(i['distance'])
                del i['category_group_code'], i['category_group_name'], i['category_name'], i['id'], i['x'], i[
                    'y']
                place_list.append(i)

            place_list.sort(key=lambda x: x['distance'])

            place_data = {'placeList': place_list}

            # /moviesearch?ip=211.106.150.88&movieNm=하모니


            # kobis - ranking
            today = datetime.datetime.now()  # 오늘날짜
            delta = datetime.timedelta(days=-1)  # 하루 전을 의미하는 timedelta객체
            yesterday = today + delta  # 오늘 날짜와 timedelta 연산
            yesterday_str = yesterday.strftime("%Y%m%d")  # yyyymmdd 형식 문자열로 변환

            for i in places:
                place_tmp = i["address_name"].split()

            placeNm = places_detail[place_tmp[0]]

            rank_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage=5&key=" + kobis_key + "&targetDt=" + yesterday_str + "&wideAreaCd=" + placeNm

            req = urllib.request.Request(rank_url)
            response = urllib.request.urlopen(req)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = response.read()
                ranking = response_body.decode('utf-8')

                rank_data = json.loads(ranking)

                for i in rank_data["boxOfficeResult"]["dailyBoxOfficeList"]:
                    del i["rnum"], i["rankInten"], i["rankOldAndNew"], i["movieCd"], i["salesAmt"], i["salesShare"], i["salesInten"], i["salesChange"], i["salesAcc"], i["audiCnt"], i["audiInten"], i["audiChange"], i["showCnt"], i["scrnCnt"]


                dict_result = {'cinePosition':place_data, 'boxOfficeRank':rank_data["boxOfficeResult"]}

                json_result = json.dumps(dict_result, ensure_ascii=False, indent=4, sort_keys=True)

                result = make_response(json_result)

            return result

        except Exception as e:
            return {'error': str(e)}


app = Flask('My First App')
api = Api(app)

api.add_resource(movieInfo, '/moviesearch/movieinfo')
api.add_resource(cineInfo, '/moviesearch/cineinfo')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "5000")


