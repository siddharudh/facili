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


% import facili
% syslog = facili.get_data('logs._syslog').get('logs._syslog')
% kernlog = facili.get_data('logs._kernlog').get('logs._kernlog')


<div class="row no-gutters">
    <div class="col-12">
        <div class="card m-1">
            <div class="card-header"><strong>Syslog</strong>
            </div>
            <div class="p-3" style="height: 45vh; overflow: auto; background-color: rgba(255, 255, 255, 0.7);">
                <pre style="white-space: pre-wrap;">
                {{syslog}}
                </pre>
            </div>
        </div>
    </div>

    <div class="col-12">
        <div class="card m-1">
            <div class="card-header"><strong>Kernel log</strong>
                
            </div>
            <div class="p-3" style="height: 45vh; overflow: auto; background-color: rgba(255, 255, 255, 0.7);">
                <pre style="white-space: pre-wrap;">
                {{kernlog}}
                </pre>
            </div>
        </div>
    </div>

</div>