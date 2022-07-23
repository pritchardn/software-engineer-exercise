"""
Contains a definition of expected object types and their plural forms.
Defining this separately means editing this object changes the behaviour of the function
and the unittests simultaneously.
"""

KNOWN_TYPES_PLURALS = {
    "star": "stars",
    "galaxy": "galaxies",
    "supernova": "supernovae",
    "nebula": "nebulae",
    "frb": "frbs",
}
