import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write('Hello, -	Công tác !')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True) 