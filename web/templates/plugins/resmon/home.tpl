% import facili
% data = facili.get_data('resmon')

<div class="row no-gutters">
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card mr-3 mb-3">
            <div class="card-header"><strong>CPU</strong>
                
            </div>
            <div class="chart-body py-3" style="height: 20vh;">
                <canvas id="live-cpu-chart">
                </canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card mr-3 mb-3">
            <div class="card-header"><strong>Load</strong>
            </div>
            <div class="chart-body" style="height: 20vh;">
                <canvas id="live-load-chart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card mr-3 mb-3">
            <div class="card-header"><strong>Memory</strong>
            </div>
            <div class="chart-body py-3" style=" height: 20vh">
                <canvas id="live-mem-chart">
                </canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card mr-3 mb-3">
            <div class="card-header"><strong>Disk space</strong>
            </div>
            <div class="table-responsive" style=" height: 20vh;">
                %
                <table class="table" style="font-size: 0.8em">
                  % disks = data['resmon.live.disk']
                  % for d in disks:
                  <tr><td style="padding-top: 5px; padding-bottom: 5px;font-size: 0.9em;">{{d}}<br><progress value="{{disks[d]['percent']}}" style="height: 15px; width: 100%; -webkit-appearance: none; -moz-appearance: none; " max="100"></td></tr>
                  % end
               </table>
            </div>
        </div>
    </div>
    <div class="col-lg-2 col-sm-4 col-6">
            <div class="card mr-3 mb-3">
                <div class="card-header"><strong>Disk I/O</strong>
                </div>
                <div class="chart-body" style="height: 20vh;">
                    <canvas id="live-dio-chart"></canvas>
                </div>
            </div>
        </div>
    <div class="col-lg-2 col-sm-4 col-6">
        <div class="card mr-3 mb-3">
            <div class="card-header"><strong>Network I/O</strong>
            </div>
            <div class="chart-body" style="height: 20vh;">
                <canvas id="live-net-chart"></canvas>
            </div>
        </div>
    </div>
</div>






<script type="text/javascript" src="/static/js/moment.min.js"></script>
<script type="text/javascript" src="/static/js/chart.min.js"></script>

<script type="text/javascript" src="/static/js/plugins/resmon/chart-loader.js"></script>