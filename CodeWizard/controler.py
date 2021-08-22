# 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
import web

urls = (
    '/', 'home'
)

render = web.template.render("views/Templates/", base="MainLayout")
app = web.application(urls, globals())

class home:
    def GET(self):
        return render.Home()


if __name__ == "__main__":
    app.run()

print("go to" , 'http://localhost:8080')