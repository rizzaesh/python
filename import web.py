# 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
import web

urls = (
    '/(.*)/(.*)', 'index'
)

render = web.template.render("resources/")
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return render.main(name,age)


if __name__ == "__main__":
    app.run()