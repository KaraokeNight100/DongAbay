from google.appengine.api import users

import webapp2

class MainHandler(webapp2.RequestHandler):

    def get(self):
        # Display the picture
        self.response.write('<html><header><body>')
        self.response.write('<img src="http://2.bp.blogspot.com/-Xday0Ic8AVw/UIdVzblVhRI/AAAAAAAABNQ/uAQaft84TXI/s1600/DSC_3094.jpg">')
        self.response.write('</body></header></html>')
        
application = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)    
        
