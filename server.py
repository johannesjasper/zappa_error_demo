import logging
from wsgiref import simple_server

import falcon
from falcon import Request, Response
from pydantic import BaseModel
from zappa.asynchronous import task

import config


class DemoRequest(BaseModel):
    foo: str
    bar: str


class DemoController:

    def on_post(self, req: Request, resp: Response):
        short_running_task(req.media)
        resp.status = falcon.HTTP_202

    def on_post_async(self, req: Request, resp: Response):
        long_running_task(req.media)
        resp.status = falcon.HTTP_202


def short_running_task(request_data: dict):
    request = DemoRequest(**request_data)
    logging.info(f'Received request: {request}')


@task
def long_running_task(request_data: dict):
    request = DemoRequest(**request_data)
    logging.info(f'Received request: {request}')


falcon_app = falcon.API()
demo_controller = DemoController()
falcon_app.add_route('/demo', demo_controller)
falcon_app.add_route('/asyncdemo', demo_controller, suffix='async')

if __name__ == '__main__':
    httpd = simple_server.make_server(config.SERVER_HOST, int(config.SERVER_PORT), falcon_app)
    httpd.serve_forever()
