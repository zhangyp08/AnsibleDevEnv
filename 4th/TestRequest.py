import json
import requests
from log import logger

hlist = []

header = {
    'content-type': "application/json;charset=UTF-8"
}


def TestPostRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthop):
    hr = requests.post(hurl, data=hdata, headers=headers)
    hresult = json.loads(hr.text)
    hstatus = hresult['status']
    hhhdata = {
        "t_id": htestcaseid,
        "t_name": htestcasename,
        "t_method": "POST",
        "t_url": hurl,
        "t_param": "test data: " + str(hdata),
        "t_hope": "status: " + htesthope + " expected result: " + fanhuitesthop,
        "t_actual": "status: " + hstatus + " expected result: " + str(hresult)
    }
    if hstatus == htesthope and fanhuitesthop in str(hresult):
        hhhdata['t_result'] = "PASS"
        logger.info(htestcasename)
        logger.info("PASS")
        logger.info("Actual result:" + str(hresult))
    else:
        hhhdata['t_result'] = "FAIL"
        logger.error(htestcasename)
        logger.error("FAIL")
        logger.error("Actual result:" + str(hresult))

    hlist.append(hhhdata)
    print(hlist)

def TestGetRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthop, st):
    if hdata:
        hr = requests.get(hurl, params=hdata, headers=headers)
    else:
        hr = requests.get(hurl, headers=headers)

    hresult = json.loads(hr.text)
    hstatus = hresult[st]
    hhhdata = {
        "t_id": htestcaseid,
        "t_name": htestcasename,
        "t_method": "Get",
        "t_url": hurl,
        "t_param": "test data: " + str(hdata),
        "t_hope": "status: " + htesthope + " expected result: " + fanhuitesthop,
        "t_actual": "status: " + str(hstatus) + " expected result: " + str(hresult)
    }
    if str(hstatus) == htesthope and fanhuitesthop in str(hresult):
        hhhdata['t_result'] = "PASS"
        logger.info(htestcasename)
        logger.info("PASS")
        logger.info("Actual result:" + str(hresult))
    else:
        hhhdata['t_result'] = "FAIL"
        logger.error(htestcasename)
        logger.error("FAIL")
        logger.error("Actual result:" + str(hresult))

    hlist.append(hhhdata)
    print(hlist)


def TestDeleteRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthop):
    hr = requests.delete(hurl, params=hdata, headers=headers, )
    hresult = json.loads(hr.text)
    hstatus = hresult['status']
    hhhdata = {
        "t_id": htestcaseid,
        "t_name": htestcasename,
        "t_method": "Delete",
        "t_url": hurl,
        "t_param": "test data: " + str(hdata),
        "t_hope": "status: " + htesthope + " expected result: " + fanhuitesthop,
        "t_actual": "status: " + hstatus + " expected result: " + str(hresult)
    }
    if hstatus == htesthope and fanhuitesthop in str(hresult):
        hhhdata['t_result'] = "PASS"
        logger.info(htestcasename)
        logger.info("PASS")
        logger.info("Actual result:" + str(hresult))
    else:
        hhhdata['t_result'] = "FAIL"
        logger.error(htestcasename)
        logger.error("FAIL")
        logger.error("Actual result:" + str(hresult))

    hlist.append(hhhdata)
    print(hlist)

