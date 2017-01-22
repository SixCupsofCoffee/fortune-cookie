#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_paragraph = "<p>" + fortune + "</p>"
        fortune_sentence = "Your fortune: " + fortune

        luckyNumber = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        numberSentence = 'Your lucky number: ' + luckyNumber
        numberParagraph = "<p>" + numberSentence + "</p>"

        newCookieButton = "<a href='.'><button>Another cookie please!</button></a>"

        content = header + fortune_sentence + numberParagraph + newCookieButton


        self.response.write(content)

def getRandomFortune():
    # list of fortunes
    fortunes = [
        "I see much code in your future",
        "Consider eating more fortunes cookies",
        "You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
    ]

    # randomly select one of the fortunes
    index = random.randint(0,2)

    return fortunes[index]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
