def company(*founders):
    staff = set(founders)

    def hire(m):
        if type(m) is str and m.isalpha():
            staff.add(m)
        else:
            raise ValueError("name must be made up of alphabets only.")

    def fire(m):
        if m in founders:
            raise ValueError("Cannot fire founding members!")
        staff.remove(m)

    def show():
        return ", ".join(staff)

    return hire, fire, show
