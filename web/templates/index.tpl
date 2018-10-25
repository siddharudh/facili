<!DOCTYPE html>
<html lang="en">
<head>
  <title>Facili</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="/static/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/facili.css">
  <script src="/static/js/jquery.min.js"></script>
  <script src="/static/js/popper.min.js"></script>
  <script src="/static/js/bootstrap.min.js"></script>
</head>
<body>
  <div class="container-fluid">
    <div style="float: right;">
      <h1 style="font-weight:300;line-height:0.4;color:coral;">Facili</h1>
      <small style="display:inline;color:#aaa">&nbsp;easy info tool</small>
    </div>
    <ul class="nav nav-tabs" role="tablist">
      % for i, plugin_id in enumerate(plugins):
        <li class="nav-item">
          <a class="nav-link{{' active' if i == 0 else ''}}" data-toggle="tab" href="#{{plugin_id}}" role="tab" aria-controls="{{plugin_id}}" aria-selected="{{'true' if i == 0 else 'false'}}">{{plugins[plugin_id][0]}}</a>
        </li>
      % end
    </ul>
    <div class="tab-content">
      % for i, plugin_id in enumerate(plugins):
        <div id="{{plugin_id}}" class="container-fluid tab-pane fade{{' show active' if i == 0 else ''}}" role="tabpanel" aria-labelledby="{{plugin_id}}-tab"><br>
          <h3>{{plugins[plugin_id][0]}}</h3>
          <p>{{plugins[plugin_id][1]}}</p>
          % include('plugins/' + plugin_id + '/home.tpl')
        </div>
      % end
    </div>
  </div>
  <script>
    const lightColors = [ "Snow", "Honeydew", "Azure", "OldLace",
                    "GhostWhite", "Ivory", "WhiteSmoke", "AliceBlue",  "Beige",
                    "MintCream",  "Seashell", "LavenderBlush",
                    "AntiqueWhite", "FloralWhite", "Linen", "MistyRose"];
    $(".card").each(function(index) {
      $(this).css('background-color', lightColors[index % lightColors.length]);
    });
  </script>
</body>
</html>