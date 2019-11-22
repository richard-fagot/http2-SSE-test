<template>
  <div>
    <h1>Data Streamer Of The Killing Death</h1>

    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>

    <button v-on:click="refreshData()">Refresh</button>
    <div id="target_div">Watch this space...</div>
  </div>
</template>

<script>
import axios from 'axios';
import { Plotly } from 'vue-plotly';

// const targetContainer = document.getElementById('target_div');
const eventSource = new EventSource('http://localhost:5000/stream');
eventSource.onmessage = function (e) {
  document.getElementById('target_div').innerHTML = e.data;
};

export default {
  name: 'DataStreamerChart',
  components: {
    Plotly,
  },
  data() {
    return {
      data: [{
        x: '',
        y: '',
        type: 'scatter',
      }],
      layout: {
        title: 'My graph',
      },
    };
  },

  methods: {
    refreshData() {
      const path = 'http://localhost:5000/data';
      axios.get(path)
        .then((res) => {
          this.data[0].y = res.data.y;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.refreshData();
  },
};
</script>
