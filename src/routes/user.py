from utils.utils import sendData

async def _list_users(req):
    """List all users
    """
    body = {'method': req.method}
    return sendData(req, body)


async def _get_user(req):
    """Get one user
    """
    # add call back func
    def cb(r):
        print('/user GET')
    req.add_done_callback(cb)

    params = req.match_dict
    body = params
    return sendData(req, body)


async def _add_user(req):
    """Add one user
    """
    body = {'method': req.method}
    return sendData(req, body)


# add route
def user_route(router):
    router.add_route('/user', _list_users, 'GET')
    router.add_route('/user/{uid}', _get_user, 'GET')
    router.add_route('/user', _add_user, 'POST')
