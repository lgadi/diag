import logging
import subprocess
import threading
import os.path

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class UploadHandler(BaseHandler):

    def get_command_name(self):
        return "upload"

    def run(self, command, command_args, command_id):
        super().run(command, command_args, command_id)
        print("command is: " + command + ", uploading file from:" + command_args[0] + ", command number: " + str(command_id))
        file_path = os.path.normpath(command_args[0])
        if os.path.exists(file_path):
            out_file = open(file_path,"r")
            out = out_file.read()
            self.post_result(out)
            out_file.close()
