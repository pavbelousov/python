# -*- coding: utf-8 -*-

"""
This module contains all the commands we work with.
If you want to create a new command it should be placed here.
"""

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import (
    BaseItem,
    ToDoItem,
    ToBuyItem,
)
from utils import get_input_function

__author__ = 'sobolevn'


class BaseCommand(object):
    """
    Main class for all the commands.
    Defines basic method and values for all of them.
    Should be subclassed to create new commands.
    """

    @staticmethod
    def label():
        """
        This method is called to get the commands short name:
        like `new` or `list`.
        """
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        """
        This method is called to run the command's logic.
        """
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        # Dynamic load:
        # def class_filter(klass):
        #     return inspect.isclass(klass) \
        #            and klass.__module__ == BaseItem.__module__ \
        #            and issubclass(klass, BaseItem) \
        #            and klass is not BaseItem
        #
        # classes = inspect.getmembers(
        #         sys.modules[BaseItem.__module__],
        #         class_filter,
        # )
        classes = {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
        }
        return dict(classes)

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                break
            except ValueError:
                print('Bad input, try again.')

        selected_key = list(classes.keys())[selection]
        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')


class ToReadItem(BaseItem):
    def __init__(self):
        pass
