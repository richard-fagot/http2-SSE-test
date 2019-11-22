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

/*
// const targetContainer = document.getElementById('target_div');
const eventSource = new EventSource('http://localhost:5000/stream');
eventSource.onmessage = function (e) {
  document.getElementById('target_div').innerHTML = e.data;
  this.refreshData();
};
*/

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
    setY(y) {
      this.data[0].y = y;
    },

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

    setupStream() {
      // Not a real URL, just using for demo purposes
      const es = new EventSource('http://localhost:5000/stream');
      // const that = this;
      es.onmessage = (e) => {
        document.getElementById('target_div').innerHTML = e.data;
        const msg = JSON.parse(e.data);
        this.data[0].y = msg.y;
      };
      /*
      es.addEventListener('message', event => {
        let data = JSON.parse(event.data);
        this.stockData = data.stockData;
      }, false);
      */
    },
  },

  created() {
    this.refreshData();
    this.setupStream();
  },
};
</script>
