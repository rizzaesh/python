# 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
import web

urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:
    def GET(self, name):
        if not name:
            name = 'World'
        return '<h1>Hello</h1>, ' + name + '!'

if __name__ == "__main__":
    app.run()