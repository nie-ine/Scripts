#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
definition of class knora-base:Resource
"""


class Resource(object):
    """

    """

    _ontology = "http://www.knora.org/ontology"
    _project = "http://data.knora.org/projects"

    def __init__(self, label, seqnum=None):
        self._namespace = "knora-base"
        self._name = "Resource"
        self._label = label
        self.seqnum = seqnum

    def __getattribute__(self, item):
        """

        :param item:
        :return:
        """
        try:
            return object.__getattribute__(self, item)._value
        except AttributeError as e:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        try:
            object.__getattribute__(self, key)._value = value
        except Exception as e:
            return object.__setattr__(self, key, value)

    def json(self):
        """

        :return:
        """

        restype_id = "{:s}/{:s}#{:s}".format(self._ontology, self._namespace, self._name)
        project_id = "{:s}/{:s}".format(self._project, self._namespace)
        properties = {}
        for attr, value in self.__dict__.items():
            if value is None or attr.startswith('_'):
                continue
            try:
                if value._value is None:
                    continue
                properties[value.key()] = value.json()
            except Exception:
                pass

        if self.seqnum == 0 or self.seqnum:
            key = 'http://www.knora.org/ontology/knora-base#seqnum'
            properties[key] = [{'int_value': self.seqnum}]

        return {'restype_id': restype_id,
                'label': self._label,
                'project_id': project_id,
                'properties': properties}

    def __getitem__(self, item):
        """

        :return:
        """

        return item._value

    def __repr__(self):
        return "{}".format(self.json())

    def __str__(self):
        return "{}".format(self.json())
