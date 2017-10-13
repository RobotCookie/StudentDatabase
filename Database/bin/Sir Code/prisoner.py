# the prisoner class
class Prisoner:
    id              = 0
    title           = ""
    firstname       = ""
    middlename      = ""
    lastname        = ""
    sentenceType    = ""

    def __repr__(self):
        return id

    def __str__(self):
        str = "({5}) {0} {1} {2} {3} [{4}]"
        str = str.format(self.title, self.firstname, self.middlename, self.lastname, self.sentenceType, self.id)
        str = str.strip()
        str = str.replace("  ", " ")
        return str
