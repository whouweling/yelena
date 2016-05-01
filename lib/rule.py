
import logging

rules = []


class Rule:

    def __init__(self, name, conditions, actions):
        self.name = name
        self.conditions = conditions
        self.actions = actions
        self.active = None
        rules.append(self)
        logging.info("defined rule '%s'" % self.name)

    def check(self):

        for condition in self.conditions:
            if not condition.check():
                return False

        return True

    def activate(self):
        if not self.active:
            logging.debug("activating rule '%s'" % self.name)
            for action in self.actions:
                action.execute()
