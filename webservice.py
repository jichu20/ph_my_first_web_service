# coding=utf-8

import web

urls = (
    '/paises(/.*)?', 'paises',
)

# application = web.application(urls, globals()).wsgifunc()


class paises:

    paises = {
        34: {'España', "ES"}, 33: {"Francia", "FR"}}
    codes = {
        400: '400 Bad Request',

        404: '404 Not Found',
        405: '405 Method Not Allowed',
        409: '409 Conflict'
    }

    def __init__(self):
        web.header('Content-Type', 'application/json', unique=True)

    def GET(self, pais=None):

        # return json.dumps('{"test": "test"}'    , ensure_ascii=False, encoding='utf8')
        print(pais)
        # return f'{"pais": {web.input().pais}}'
        return {"pais": web.input().pais}


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
