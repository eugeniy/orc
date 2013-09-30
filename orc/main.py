import logging
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from pkg_resources import iter_entry_points

log = logging.getLogger(__name__)

define('port', type=int, default=5067, help='server port number')
define('debug', type=bool, default=True, help='debug mode')


class PluginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(
            {'plugins': [
                {'module_name': plugin.__dict__.get('module_name'),
                 'name': plugin.__dict__.get('name')}
                for plugin in iter_entry_points(group='orc.plugin')]
            })


if __name__ == '__main__':
    options.parse_command_line()

    app = tornado.web.Application([
        (r'/api/plugins', PluginHandler),
    ],
        debug=options.debug)

    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
