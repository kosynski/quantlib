
"""
 Copyright (C) 2005, 2006, 2007 Eric Ehlers
 Copyright (C) 2005 Plamen Neykov
 Copyright (C) 2005 Aurelien Chanudet

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/license.shtml>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

"""Encapsulate enumerations for a library datatype."""

from gensrc.serialization import serializable
from gensrc.utilities import common

class EnumeratedPair(serializable.Serializable):
    """Encapsulate a library enumerated type which comprises a pair of strings
    mapped to a single enumeration."""

    #############################################
    # class variables
    #############################################

    groupName_ = 'EnumeratedPairs'

    #############################################
    # class variables
    #############################################

    def name(self):
        """Return unique identifier for this object, comprising the string pair
        in the format str1:str2."""
        return self.id1_ + ':' + self.id2_

    def id1(self):
        """Return the first string in the key pair."""
        return self.id1_

    def id2(self):
        """Return the second string in the key pair."""
        return self.id2_

    def value(self):
        """Return the enumeration value."""
        return self.value_

    #############################################
    # public interface
    #############################################

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeProperty(self, 'id1')
        serializer.serializeProperty(self, 'id2')
        serializer.serializeProperty(self, common.VALUE)

class EnumeratedPairGroup(serializable.Serializable):
    """Encapsulate a group of EnumeratedPair objects."""

    #############################################
    # class variables
    #############################################

    groupName_ = 'EnumeratedPairGroups'

    #############################################
    # public interface
    #############################################

    def className(self):
        """Return the identifier of this object's class."""
        return self.class_

    def enumeratedPairs(self):
        """Serve up enumeration definition objects alphabetically by name."""
        for key in self.enumeratedPairKeys_:
            yield self.enumeratedPairs_[key]

    def includeFile(self):
        """Return #include directive necessary to compile the source
        code autogenerated in relation to this class."""
        return self.includeFile_

    #############################################
    # serializer interface
    #############################################

    def name(self):
        """Return unique identifier for this object."""
        return self.class_

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeAttribute(self, 'class')
        serializer.serializeObjectDict(self, EnumeratedPair)
        serializer.serializeProperty(self, 'includeFile')

