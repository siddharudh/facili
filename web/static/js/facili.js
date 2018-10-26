const lightColors = [ "Snow", "Honeydew", "Azure", "OldLace",
                    "GhostWhite", "Ivory", "WhiteSmoke", "AliceBlue",  "Beige",
                    "MintCream",  "Seashell", "LavenderBlush",
                    "AntiqueWhite", "FloralWhite", "Linen", "MistyRose"];

$(".card").each(function(index) {
    $(this).css('background-color', lightColors[index % lightColors.length]);
});