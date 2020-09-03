from domainmodel.director import Director


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.colleague = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, value):
        if value == "" or type(value) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = value.strip()

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other):
        if not (isinstance(other, Actor) or other.actor_full_name is None):
            return False
        else:
            return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague:"Actor"):
        self.colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague:"Actor"):
        return colleague in self.colleague


# actor1 = Actor("Jane")
#
# director1 = Director("no")
# actor1.add_actor_colleague(actor1)
# #print(actor1.colleague)
# print(actor1.check_if_this_actor_worked_with(actor1))
