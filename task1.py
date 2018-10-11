class Developer():
    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            return "My name is " + self.name + " and I am a Junior Developer."
        elif self.years_experience <= 5:
            return "My name is " + self.name + " and I am a Middle Developer."
        else:
            return "My name is " + self.name + " and I am a Senior Developer."

    def write_code(self):
        return print("I am a developer and I write code")

    def __str__(self):
        return '%s — %s years, %s' % (self.name, self.years_experience, self.language)

    def __call__(self):
        return self.write_code()

class PythonDeveloper(Developer):
    def __init__(self, years_experience, name, language="Python"):
        Developer.__init__(self, name, years_experience)
        self.language = language

    def write_code(self):
        return "I use " + self.language + " to write code"

class JavaDeveloper(Developer):
    def __init__(self, years_experience, name, language="Java"):
        Developer.__init__(self, name, years_experience)
        self.language = language

    def write_code(self):
        return "I use " + self.language + " to write code"

class RubyDeveloper(Developer):
    def __init__(self, years_experience, name, language="Ruby"):
        Developer.__init__(self, name, years_experience)
        self.language = language

    def write_code(self):
        return "I use " + self.language + " to write code"

if __name__=='__main__':

    a = JavaDeveloper(1, 'Alex')
    print(a)
    print(a.about())
    print(a.write_code())
    print("\n")
    s = PythonDeveloper(13, 'Sam')
    print(s)
    print(s.about())
    print(s.write_code())
    print("\n")
    i = JavaDeveloper(4, 'Iwan')
    print(i)
    print(i.about())
    print(i.write_code())
    print("\n")
    j = RubyDeveloper(1, 'Jörgen')
    print(j)
    print(j.about())
    print(j.write_code())
    print("\n")
    developer = PythonDeveloper('Wasyl', 5)
    print(developer())
    developer2 = RubyDeveloper('Kolian', 5)
    print(developer2())