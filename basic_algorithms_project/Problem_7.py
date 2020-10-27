class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
        self.handler = None

    def insert(self, path, handler):
        curr_node = self.root
        for part in path:
            if part not in curr_node.children:
                curr_node.children[part] = RouteTrieNode()
            curr_node = curr_node.children[part]
        curr_node.handler = handler

    def lookup(self, path_parts):
        curr_node = self.root
        for part in path_parts:
            if part not in curr_node.children:
                return None
            else:
                curr_node = curr_node.children[part]
        return curr_node.handler


class Router:
    def __init__(self, root, handler):
        self.routes = RouteTrie()
        self.not_found = handler
        self.root_handler = root

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.routes.insert(path_parts, handler)

    def lookup(self, path):
        if path == '/':
            return self.root_handler
        path_parts = self.split_path(path)
        handler = self.routes.lookup(path_parts)
        if handler is None:
            return self.not_found
        else:
            return handler

    def split_path(self, path):
        if path[-1:] == '/':
            path = path[:-1]
        path_parts_list = path.split('/')
        return path_parts_list


# testing

def test_function(test_cases):
    for test in test_cases:
        if test[1] == test[2]:
            print("Test case " + test[0] + ": Pass!")
        else:
            print("Test case " + test[0] + ": FAIL.")


# create the router and add routes

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/shows/", "shows handler")
router.add_handler("/home/shows/archived_shows", "archived shows handler")
router.add_handler("/side_projects/films/", "films handler")
router.add_handler("/side_projects/films/short_films", "short films handler")

# root handler
tc_1 = ('1', router.lookup("/"), 'root handler')
# basic lookup
tc_2 = ('2', router.lookup("/home/about"), 'about handler')
# lookup with trailing '/' when added without one
tc_3 = ('3', router.lookup("/home/about/"), 'about handler')
# lookup with no trailing '/' when added with one
tc_4 = ('4', router.lookup("/home/shows"), 'shows handler')
# path with children with handlers that has no handler itself
tc_5 = ('5', router.lookup("/home"), 'not found handler')
# non-existant path
tc_6 = ('6', router.lookup("/home/about/me"), 'not found handler')
# path not under /home
tc_7 = ('7', router.lookup("/side_projects/films"), "films handler")

test_cases = [tc_1, tc_2, tc_3, tc_4, tc_5, tc_6, tc_7]
test_function(test_cases)
