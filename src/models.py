from mongoframes import Frame, SubFrame


class Link(Frame):

    _fields = {
        "slug",
        "ios",
        "android",
        "web"
    }


class IOS(SubFrame):

    _fields = {
        "primary",
        "fallback"
    }


class Android(SubFrame):

    _fields = {
        "primary",
        "fallback"
    }

