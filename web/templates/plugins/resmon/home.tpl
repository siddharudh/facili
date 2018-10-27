% import facili
% data = facili.get_data('resmon')

<div class="row no-gutters">
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>CPU</strong>
                
            </div>
            <div class="chart-body py-3" style="height: 25vh;">
                <canvas id="live-cpu-chart">
                </canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>Load</strong>
            </div>
            <div class="chart-body" style="height: 25vh;">
                <canvas id="live-load-chart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>Memory</strong>
            </div>
            <div class="chart-body py-3" style=" height: 25vh">
                <canvas id="live-mem-chart">
                </canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>Disk space</strong>
            </div>
            <div class="table-responsive" style=" height: 25vh;">
                <table class="table" style="font-size: 0.8em">
                  % disks = data['resmon.live.disk']
                  % for d in disks:
                  <tr><td style="padding-top: 10px; padding-bottom: 10px;font-size: 0.8em;font-weight: bold;"><span style="float: left; color:#666">{{d}}</span><span style="float: right; color:#999">Free: {{facili.human_readable_size(disks[d]['free'], 1024, 0)}}</span><br><progress value="{{disks[d]['percent']}}" style="height: 15px; width: 100%; -webkit-appearance: none; -moz-appearance: none; " max="100"></td></tr>
                  % end
               </table>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>Disk I/O</strong>
            </div>
            <div class="chart-body" style="height: 25vh;">
                <canvas id="live-dio-chart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card m-1">
            <div class="card-header"><strong>Network I/O</strong>
            </div>
            <div class="chart-body" style="height: 25vh;">
                <canvas id="live-net-chart"></canvas>
            </div>
        </div>
    </div>

    <div class="col-lg-4 col-sm-12 col-12">
        <div class="card m-1">
            <div class="card-header"><strong>Top 5 CPU%</strong>
            </div>
            <div class="card-body table-responsive" style="height: 25vh;">
                <table id="top5-cpu" class="table table-sm">
                    <thead>
                        <tr><th>Process</th><th>PID</th><th>CPU%</th><th>Threads</th></tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>
    </div>


    <div class="col-lg-4 col-sm-12 col-12">
        <div class="card m-1">
            <div class="card-header"><strong>Top 5 Mem%</strong>
            </div>
            <div class="card-body table-responsive" style="height: 25vh;">
                <table id="top5-mem" class="table table-sm">
                    <thead>
                        <tr><th>Process</th><th>PID</th><th>Mem%</th><th>RSS</th></tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="col-lg-4 col-sm-6 col-12">
        <div class="card m-1">
            <div class="card-header"><strong>Top 5 I/O</strong>
            </div>
            <div class="card-body table-responsive" style="height: 25vh;">
                <table id="top5-io" class="table table-sm">
                    <thead>
                        <tr><th>Process</th><th>PID</th><th>Reads</th><th>Writes</th></tr>
                    </thead>
                    <tbody></tbody>
                </table>
            </div>
        </div>
    </div>

</div>

<script type="text/javascript" src="/static/js/moment.min.js"></script>
<script type="text/javascript" src="/static/js/chart.min.js"></script>

<script type="text/javascript" src="/static/js/plugins/resmon/charts-loader.js"></script>
<script type="text/javascript" src="/static/js/plugins/resmon/tables-loader.js"></script>
<script type="text/javascript" src="/static/js/plugins/resmon/live-data-loader.js"></script>
