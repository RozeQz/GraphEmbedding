from src.api.groups_controller import get_group_by_id, get_user_groups
from src.education.group import Group


class User():
    def __init__(self, user_id, role, firstname, lastname, midname,
                 group=None):
        self.id = user_id
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.midname = midname
        self.groups = []

        if group is not None:
            self.groups.append(group)
        else:
            groups = get_user_groups(self.id)
            for group in groups:
                group = get_group_by_id(group["group_id"])
                self.groups.append(Group(group["id"], group["name"]))
