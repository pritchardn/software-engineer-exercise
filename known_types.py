"""
Contains a definition of expected object types and their plural forms.
Defining this separately means editing this object changes the behaviour of the function
and the unittests simultaneously.
"""

known_types_plurals = {
    "star": "stars",
    "galaxy": "galaxies",
    "supernova": "supernovae",
    "nebula": "nebulae",
    "frb": "frbs",
}
