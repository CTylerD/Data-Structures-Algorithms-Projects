class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user in group.users:
        return True
    else:
        for sub_group in group.groups:
            if is_user_in_group(user, sub_group):
                return True


# build group/user structure
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child_user = "sub_child_user2"
sub_child2.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)

parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
child.add_group(sub_child2)
parent.add_group(child)


# test case 1 - user exists in group
test_case_1 = is_user_in_group("sub_child_user", parent)
if test_case_1:
    print("Test 1: Pass!")
else:
    print("Test 1: FAIL.")

# test case 2 - user exists, but not in group
test_case_2 = is_user_in_group("parent_user", child)
if not test_case_2:
    print("Test 2: Pass!")
else:
    print("Test 2: FAIL.")

# test case 3 - user does not exist
test_case_3 = is_user_in_group("wrong_user", parent)
if not test_case_3:
    print("Test 3: Pass!")
else:
    print("Test 3: FAIL.")
