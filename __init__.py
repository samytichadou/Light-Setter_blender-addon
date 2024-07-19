'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


# IMPORT SPECIFICS
##################################

from . import   (
    gui,
    select_light_operator,
    properties,
    addon_prefs,
)


# register
##################################

def register():
    gui.register()
    select_light_operator.register()
    properties.register()
    addon_prefs.register()

def unregister():
    gui.unregister()
    select_light_operator.unregister()
    properties.unregister()
    addon_prefs.unregister()
