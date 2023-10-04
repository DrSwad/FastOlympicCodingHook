import sublime
import sublime_plugin
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import _thread
import threading
import platform
from os import path

def MakeHandlerClassFromFilename(file_full_path, tests_relative_dir, tests_file_suffix):
    if not tests_file_suffix: tests_file_suffix = "__tests"

    class HandleRequests(BaseHTTPRequestHandler):
        def do_POST(self):
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                tests = json.loads(body.decode('utf8'))
                tests = tests["tests"]
                ntests = []
                for test in tests:
                    ntest = {
                        "test": test["input"],
                        "correct_answers": [test["output"].strip()]
                    }
                    ntests.append(ntest)
                file_relative_dir = path.dirname(file_full_path)
                file_name = path.basename(file_full_path)
                nfilename = path.join(file_relative_dir, tests_relative_dir, file_name + tests_file_suffix) \
                    if tests_relative_dir else path.join(file_relative_dir, file_name + tests_file_suffix)
                print("New test case path: " + nfilename)
                with open(nfilename, "w") as f:
                    f.write(json.dumps(ntests))
            except Exception as e:
                print("Error handling POST - " + str(e))
            threading.Thread(target=self.server.shutdown, daemon=True).start()
    return HandleRequests


class CompetitiveCompanionServer:
    def startServer(file_full_path, foc_settings):
        host = 'localhost'
        port = 12345
        tests_relative_dir = foc_settings.get("tests_relative_dir")
        tests_file_suffix = foc_settings.get("tests_file_suffix")
        HandlerClass = MakeHandlerClassFromFilename(file_full_path, tests_relative_dir, tests_file_suffix)
        httpd = HTTPServer((host, port), HandlerClass)
        httpd.serve_forever()
        print("Server has been shutdown")


class FastOlympicCodingHookCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            _thread.start_new_thread(CompetitiveCompanionServer.startServer,
                                     (self.view.file_name(),
                                      sublime.load_settings("FastOlympicCoding.sublime-settings")))
        except Exception as e:
            print("Error: unable to start thread - " + str(e))
