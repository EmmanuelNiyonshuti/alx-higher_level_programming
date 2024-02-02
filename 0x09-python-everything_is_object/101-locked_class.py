#!/usr/bin/python3

class LockedClass:

    __slot__ = ["first_name"]

    def  __setattr__(self, name, value):
            if name != "first_name":
                raise AttributeError("LockedClass has no attribute '{}'".format(name))
            super().__setattr__(name, value)
