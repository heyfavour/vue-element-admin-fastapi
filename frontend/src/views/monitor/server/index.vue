<template>
  <div class="app-container">
    <el-row>
      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span>CPU</span></div>
          <div v-loading="loading" class="el-table el-table--enable-row-hover el-table--medium">
            <table cellspacing="0" style="width: 100%;">
              <thead>
                <tr>
                  <th class="is-leaf">
                    <div class="cell">属性</div>
                  </th>
                  <th class="is-leaf">
                    <div class="cell">值</div>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="cell">核心数</div>
                  </td>
                  <td>
                    <div v-if="server.cpu" class="cell">{{ server.cpu.cpuNum }}</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">用户使用率</div>
                  </td>
                  <td>
                    <div v-if="server.cpu" class="cell">{{ server.cpu.used }}%</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">进程数</div>
                  </td>
                  <td>
                    <div v-if="server.cpu" class="cell">{{ server.cpu.pids }}</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">系统使用时间</div>
                  </td>
                  <td>
                    <div v-if="server.cpu" class="cell">{{ server.cpu.boot_time }}H</div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>

      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span>内存</span></div>
          <div v-loading="loading" class="el-table el-table--enable-row-hover el-table--medium">
            <table cellspacing="0" style="width: 100%;">
              <thead>
                <tr>
                  <th class="is-leaf">
                    <div class="cell">属性</div>
                  </th>
                  <th class="is-leaf">
                    <div class="cell">内存</div>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="cell">总内存</div>
                  </td>
                  <td>
                    <div v-if="server.mem" class="cell">{{ server.mem.total }}G</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">已用内存</div>
                  </td>
                  <td>
                    <div v-if="server.mem" class="cell">{{ server.mem.used }}G</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">剩余内存</div>
                  </td>
                  <td>
                    <div v-if="server.mem" class="cell">{{ server.mem.free }}G</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="cell">使用率</div>
                  </td>
                  <td>
                    <div v-if="server.mem" class="cell" :class="{'text-danger': server.mem.percent > 80}">{{
                      server.mem.percent }}%
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import io from 'socket.io-client'

export default {
  name: 'Server',
  data() {
    return {
      // 加载层信息
      loading: true,
      // 服务器信息
      server: { cpu: {}}
    }
  },
  created() {
    const _this = this
    _this.loading = true
    this.socket = io('http://127.0.0.1:8080/server', {
      transports: ['websocket']
    })
    this.socket.emit('connect')
    this.socket.on('monitor_server', function(data) {
      if (_this.loading) {
        _this.loading = false
        _this.server.cpu = data.cpu_info
        _this.server.mem = data.memory_info
      } else {
        _this.server.cpu = data.cpu_info
        _this.server.mem = data.memory_info
      }
    })
  },
  methods: {}
}
</script>
