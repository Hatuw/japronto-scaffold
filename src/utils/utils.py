async def sendData(req, body, status_code=200):
    res = {}
    res['code'] = status_code
    res['status'] = 'success' if status_code == 200 else 'failed'
    res['data'] = body
    return req.Response(
        code=status_code,
        json=res
    )
