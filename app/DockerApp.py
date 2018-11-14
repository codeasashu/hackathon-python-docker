# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import docker
from pprint import pprint

class DockerApp:

    def __init__(self):
        self.images = {}
        self.client = None

    def init(self):
        pprint("Initializing....")
        try:
            self.client = docker.from_env()
            pprint(self.client.info())
        except Exception as ex:
            #log exception
            raise ex
    def image(self):
        for image in self.client.images.list():
            pprint(image)
