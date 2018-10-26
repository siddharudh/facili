// facili - easy info tool web frontend

// Copyright (C) 2018 Siddharudh P T

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 2.1 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.

// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>


const lightColors = [ "Snow", "Honeydew", "Azure", "OldLace",
                    "GhostWhite", "Ivory", "WhiteSmoke", "AliceBlue",  "Beige",
                    "MintCream",  "Seashell", "LavenderBlush",
                    "AntiqueWhite", "FloralWhite", "Linen", "MistyRose"];

$(".card").each(function(index) {
    $(this).css('background-color', lightColors[index % lightColors.length]);
});