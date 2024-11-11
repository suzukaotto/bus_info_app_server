import datetime
import json

def get_now_isotime():
    return datetime.datetime.now().isoformat()

def get_response(_code, data:any=None) -> dict:
    _code = str(_code)
    
    with open('./error.json', 'r') as f:
        error_infos = json.load(f)

    f_response = {
        "response": {
            "header": {
                "queryTime": get_now_isotime(),
                "resultCode": _code,
                "resultMessage": error_infos.get(_code, "Unknown status")
            },
            "body": {
                "result": None
            }
        }
    }
    
    if data is not None:
        f_response["response"]["body"]["result"] = data
    
    return f_response

def detect_response_error(_res_dict:dict, _df_code:str='-1', _df_msg:str='Unknown status') -> tuple:     
    'return: (res_code, res_msg)'
    
    # Normal Response
    if "response" in _res_dict:
        msg_header = _res_dict["response"]["msgHeader"]
        res_code = msg_header.get("resultCode", _df_code)
        res_msg = msg_header.get("resultMessage", _df_msg)
        return (res_code, res_msg, 'normal')
    
    # OpenAPI Response
    elif "OpenAPI_ServiceResponse" in _res_dict:
        msg_header = _res_dict["OpenAPI_ServiceResponse"]["cmmMsgHeader"]
        res_code = msg_header.get("returnReasonCode", _df_code)
        res_msg = msg_header.get("errMsg", _df_msg)
        return (res_code, res_msg, 'openapi')
    
    # Unknown Response
    else:
        return (_df_code, _df_msg, 'unknown')
    
def process_search_data(_res_dict: dict):
    detect_rst = detect_response_error(_res_dict)
    
    if detect_rst[2] == 'normal':
        if detect_rst[0] == '1':
            return get_response(21)
        elif detect_rst[0] == '2':
            return get_response(10)
        elif detect_rst[0] == '3':
            return get_response(11)
        elif detect_rst[0] == '20':
            return get_response(13)
        elif detect_rst[0] in ['0', '00', '4']:
            pass
        else:
            return get_response(21)
    
    if 'msgBody' in _res_dict['response']:
        pcsd_data = _res_dict['response']['msgBody']
    else:
        pcsd_data = None
    
    if detect_rst[0] == '4':
        return get_response(16, pcsd_data)
    
    return get_response(0, pcsd_data)