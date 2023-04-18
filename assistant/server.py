from wsgiref.simple_server import make_server

from . import action, bashscript 

import abc
import datetime
import falcon
import requests



class ActionResource(abc.ABC):

    def on_post(self, req, resp):
        """Handles POST requests"""
        req_obj = req.get_media()
        original_text = req_obj["text"]
        if not original_text:
            resp.status = falcon.HTTP_403
            return

        updated_text = action.isAction(original_text)
        resp.status = falcon.HTTP_200
        isaction = (updated_text.lower()=="true")
        resp.media = {"result": isaction}


class CommandResource(abc.ABC):

    def on_post(self, req, resp):
        """Handles POST requests"""
        req_obj = req.get_media()
        original_text = req_obj["text"]
        if not original_text:
            resp.status = falcon.HTTP_403
            return

        updated_text = bashscript.returnBashForGivenAction(original_text)
        resp.status = falcon.HTTP_200
        resp.media = {"command:": updated_text}



app = falcon.App(cors_enable=True)

is_action = ActionResource()
command_resource = CommandResource()

app.add_route("/action", is_action)
app.add_route("/command", command_resource)

if __name__ == "__main__":
    with make_server("", 8080, app) as httpd:
        print("Serving on port 8080...")

        # Serve until process is killed
        httpd.serve_forever()

