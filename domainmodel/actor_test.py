from domainmodel.actor import Actor


class TestDirectorMethods:

    def test_init(self):
        actor1 = Actor("Taika Waititi")
        assert repr(actor1) == "<Actor Taika Waititi>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(3)
        assert actor3.actor_full_name is None
        actor1.actor_full_name = "josie"
        assert actor1.actor_full_name == "josie"
        assert (actor1 == actor3) == False
