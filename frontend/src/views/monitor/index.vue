<template>
  <div class="app-container">
    <template v-if="isConnected">
      <p>Connected!</p>
    </template>
    <button @click="test_socket" />
  </div>
</template>

<script>

export default {
  name: 'Monitor',
  data() {
    return {
      isConnected: false
    }
  },
  created() {
  },
  sockets: {
    connect() {
      console.log('connected')
      this.isConnected = true
      this.$socket.emit('JOIN', this.roomName)
    },

    disconnect() {
      this.isConnected = false
    },

    joined_room() {
      console.log('joined room')
    }
  },
  mounted() {
  },
  // socket
  methods: {
    test_socket() {
      this.$socket.emit('YEET')
    }
  }
}
</script>
