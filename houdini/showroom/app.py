import web
import model
import json

urls = (
    '/', 'index',
    '/api/render', 'api'
)


render = web.template.render("templates/")

class index:
    def GET(self):
       return render.index()

class api:
    def GET(self):
        model.render()
        web.header('Content-Type', 'application/json')
        return json.dumps({"success": True})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
