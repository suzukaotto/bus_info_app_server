import os
from flask import Blueprint, request
import requests
import json
import xmltodict
from dotenv import load_dotenv
import utils

# load setting
load_dotenv()
with open('./error.json', 'r') as f:
    ERROR_INFOS = json.load(f)

SERVICE_KEY = os.getenv('SERVICE_KEY')

businfo_bp = Blueprint('businfo', __name__, url_prefix='/businfo')

station_bp = Blueprint('businfo_station_bp', __name__, url_prefix='/station')
businfo_bp.register_blueprint(station_bp)

bus_bp = Blueprint('businfo_bus_bp', __name__, url_prefix='/bus')
businfo_bp.register_blueprint(bus_bp)


@station_bp.route('/search/keyword', methods=['GET'])
def search_keyword():
    _req_url = "https://apis.data.go.kr/6410000/busstationservice/getBusStationList"
    res_keyword = request.args.get('keyword', None)
    
    if res_keyword is None:
        return utils.get_response(10)
    
    # processing
    try:
        res = requests.get(_req_url, params={'serviceKey': SERVICE_KEY, 'keyword': res_keyword})
        res_dict = xmltodict.parse(res.text)
    except:
        return utils.get_response(21)
    
    detect_rst = utils.process_search_data(res_dict)
    
    return detect_rst
    
@station_bp.route('/search/coor', methods=['GET'])
def search_coor():
    _req_url = "https://apis.data.go.kr/6410000/busstationservice/getBusStationAroundList"
    res_x = request.args.get('x', None)
    res_y = request.args.get('y', None)
    
    if res_x is None or res_y is None:
        return utils.get_response(10)
    
    # processing
    try:
        res = requests.get(_req_url, params={'serviceKey': SERVICE_KEY, 'x': res_x, 'y': res_y})
        res_dict = xmltodict.parse(res.text)
    except:
        return utils.get_response(21)
    
    detect_rst = utils.process_search_data(res_dict)
    
    return detect_rst

@station_bp.route('/search/arvlbus', methods=['GET'])
def search_arvlbus():
    _req_url = "https://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList"
    res_station_id = request.args.get('stationId', None)
    
    if res_station_id is None:
        return utils.get_response(10)
    
    # processing
    try:
        res = requests.get(_req_url, params={'serviceKey': SERVICE_KEY, 'stationId': res_station_id})
        res_dict = xmltodict.parse(res.text)
    except:
        return utils.get_response(21)
    
    detect_rst = utils.process_search_data(res_dict)
    
    return detect_rst





@bus_bp.route('/search/info', methods=['GET'])
def search_bus_info():
    _req_url = "https://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem"
    res_route_id = request.args.get('routeId', None)
    
    if res_route_id is None:
        return utils.get_response(10)
    
    # processing
    try:
        res = requests.get(_req_url, params={'serviceKey': SERVICE_KEY, 'routeId': res_route_id})
        res_dict = xmltodict.parse(res.text)
    except:
        return utils.get_response(21)
    
    detect_rst = utils.process_search_data(res_dict)
    
    return detect_rst

@bus_bp.route('/search/routelist', methods=['GET'])
def search_bus_route_station():
    _req_url = "https://apis.data.go.kr/6410000/busrouteservice/getBusRouteStationList"
    res_route_id = request.args.get('routeId', None)
    
    if res_route_id is None:
        return utils.get_response(10)
    
    # processing
    try:
        res = requests.get(_req_url, params={'serviceKey': SERVICE_KEY, 'routeId': res_route_id})
        res_dict = xmltodict.parse(res.text)
    except:
        return utils.get_response(21)
    
    detect_rst = utils.process_search_data(res_dict)
    
    return detect_rst