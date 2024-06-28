import flask 

home_app = flask.Blueprint(
    name = "home",
    import_name = "app",
    template_folder = "home_page/templates",
    static_folder = "static/home_page",
    static_url_path = "/home/"
)