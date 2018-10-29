<!--
facili - easy info tool web frotend

Copyright (C) 2018 Siddharudh P T

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 2.1 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
-->



<!DOCTYPE html>
<html lang="en">
<head>
  <title>Facili</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="/static/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/facili.css">
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
        <div id="{{plugin_id}}" class="tab-pane mt-3 fade{{' show active' if i == 0 else ''}}" role="tabpanel" aria-labelledby="{{plugin_id}}-tab">
          <h3>{{plugins[plugin_id][0]}}</h3>
          <p>{{plugins[plugin_id][1]}}</p>
          % include('plugins/' + plugin_id + '/home.tpl')
        </div>
      % end
    </div>
  </div>

<!-- Scripts -->
  <script src="/static/js/jquery.min.js"></script>
  <script src="/static/js/popper.min.js"></script>
  <script src="/static/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="/static/js/facili.js"></script>

</body>
</html>