

async def _list_users(request):
    """List all users
    """
    return request.Response(text='{} User\n'.format(request.method))


async def _get_user(request):
    """Get one user
    """
    params = request.match_dict
    return request.Response(text='user id: {}\n'.format(params['uid']))


async def _add_user(request):
    """Add one user
    """
    return request.Response(text='{} user\n'.format(request.method))


# add route
def user_route(router):
    router.add_route('/user', _list_users, 'GET')
    router.add_route('/user/{uid}', _get_user, 'GET')
    router.add_route('/user', _add_user, 'POST')
