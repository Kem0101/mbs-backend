

class User:

    def __init__(self, cedula, first_name, last_name, cell_phone, email, address, role, date_born=None, province=None, electoral_college=None, electoral_college_location=None, id=None):
        self.id = id
        self.cedula = cedula
        self.first_name = first_name
        self.last_name = last_name
        self.cell_phone = cell_phone
        self.email = email
        self.address = address
        self.role = role
        self.date_born = date_born
        self.province = province
        self.electoral_college = electoral_college
        self.electoral_college_location = electoral_college_location

        def __str__(self):
            return f"{self.cedula} {self.first_name} {self.last_name} {self.cell_phone}"


class Coordinator(User):

    def __init__(self, cedula, first_name, last_name, cell_phone, email, address, role, date_born=None, province=None, electoral_college=None, electoral_college_location=None):
        super().__init__(cedula, first_name, last_name, cell_phone, email, address,
                         'coordinator', date_born, province, electoral_college, electoral_college_location)
        self.facilitators = []
        self.member_manager = MemberManager()

    def add_facilitator(self, facilitator):

        if len(self.facilitators) < 15:
            self.facilitators.append(facilitator)
        else:
            raise ValueError(
                'A coordinator cannot have more than 15 facilitators')

    def add_member(self, member):
        self.member_manager.add_member(member)


class Facilitator(User):

    def __init__(self, cedula, first_name, last_name, cell_phone, email, address, coordinator, role, date_born=None, province=None, electoral_college=None, electoral_college_location=None):
        super.__init__(cedula, first_name, last_name, cell_phone, email, address,
                       'facilitator', date_born, province, electoral_college, electoral_college_location)
        self.coordinator = coordinator
        self.member_manager = MemberManager()

    def add_member(self, member):
        self.member_manager.add_member(member)


class MemberManager:

    def __init__(self):
        self.members = []

    def add_member(self, member):

        if len(self.members) < 15:
            self.members.append(member)
        else:
            raise ValueError('Cannot have more than 15 members')
