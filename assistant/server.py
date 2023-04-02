from wsgiref.simple_server import make_server

from . import action, commands

import abc
import datetime
import falcon
import requests



class RephraseResource(abc.ABC):

    def on_post_protected(self, req, resp):
        """Handles POST requests"""
        req_obj = req.get_media()
        original_text = req_obj["text"]
        if not original_text:
            resp.status = falcon.HTTP_403
            return

        updated_text = action.isAction(original_text)
        resp.status = falcon.HTTP_200
        resp.media = {"text": updated_text}





app = falcon.App(cors_enable=True)

is_action = RephraseResource()

app.add_route("/rephrase", is_action)

if __name__ == "__main__":
    with make_server("", 8080, app) as httpd:
        print("Serving on port 8080...")

        # Serve until process is killed
        httpd.serve_forever()

