% import facili
% data = facili.get_data('sysinfo')

<div class="card-columns">
<!-- CPU -->
  <div class="card card-body">
    <h5 class="card-title">CPU</h5>
    <div class="table-responsive">
      % cpu = data['sysinfo.hw.cpu']
      <table class="table table-sm">
          <tr><th>vendor</th><td>{{cpu['vendor']}}</td></tr>
          <tr><th>model</th><td>{{cpu['model']}}</td></tr>
          <tr><th>processors</th><td>{{cpu['processors']}}</td></tr>
          <tr><th>cores</th><td>{{cpu['cores']}}</td></tr>
          <tr><th>threads</th><td>{{cpu['threads']}}</td></tr>
          <tr><th>speed</th><td>{{cpu['speed']}}</td></tr>
      </table>
    </div>
  </div>

<!-- Memory -->
  <div class="card card-body">
    <h5 class="card-title">Memory</h5>
    <div class="table-responsive">
      % mem = data['sysinfo.hw.mem']
      <table class="table table-sm">
          <tr><th>size</th><td>{{mem['size']}}</td></tr>
          <tr><th>type</th><td>{{mem['type']}}</td></tr>
          <tr><th>speed</th><td>{{mem['speed']}}</td></tr>
      </table>
    </div>
  </div>

<!-- Disks -->
<div class="card card-body">
    <h5 class="card-title">Disk Partitions</h5>
    <div class="table-responsive">
      % disks = data['sysinfo.hw.disk']
      <table class="table table-sm">
          % for d in disks:
            <tr style="color: #39f"><td>{{d['device'].replace('/dev/', '')}}</td><td></td><td></td><td>{{d['size']}}</td></tr>
            % for v in d.get('volumes', []):
              <tr><td>&nbsp;&nbsp;{{v['device'].replace('/dev/', '')}}</td><td>{{v['filesystem']}}</td><td>{{v['mountpoint']}}</td><td>{{v['size']}}</td></tr>
            % end
          % end
      </table>
    </div>
  </div>


<!-- Network -->
  <div class="card card-body">
    <h5 class="card-title">Network</h5>
    <div class="table-responsive">
      % networks = data['sysinfo.hw.net']
      <table class="table table-sm">
          % for n in networks:
            <tr><td>{{n['device']}}</td><td>{{n['address']}}</td><td>{{n['speed']}}</td></tr>
          % end
      </table>
    </div>
  </div>

<!-- Versions -->
  <div class="card card-body">
    <h5 class="card-title">Versions</h5>
    <div class="table-responsive">
      % versions = data['sysinfo.sw.ver']
      <table class="table table-sm">
          % for v in versions:
            <tr><td>{{v[0]}}</td><td>{{v[1]}}</td></tr>
          % end
      </table>
    </div>
  </div>

</div>

