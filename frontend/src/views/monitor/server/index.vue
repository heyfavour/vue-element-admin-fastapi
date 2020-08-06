<template>
  <div class="app-container">
    <template v-if="isConnected">
      <p>Connected!</p>
    </template>
    <button @click="test_socket" />
  </div>
</template>

<script>
import io from 'socket.io-client'

export default {
  name: 'Server',
  data() {
    return {
      socket: undefined,
      isConnected: false
    }
  },
  created() {
    this.socket = io('http://127.0.0.1:8080/server', {
      transports: ['websocket']
    })
  },
  methods: {
    test_socket: function() {
      console.log('111')
      const data = { 'user_id': 1111 }
      this.socket.emit('connect')
      this.socket.emit('client_message', data)
    }
  }
}
</script>
