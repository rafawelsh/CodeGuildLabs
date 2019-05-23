var self = new Vue({
  el: '#app',
  delimeters: ''[[',']]'',
  data() {
    return {
      persons: []
    }
  },
  mounted() {
    var self = this;
    axios.get('https://jsonplaceholder.typicode.com/users')
      .then(res => {
        self.persons = res.data
          console.log('Person: ', res.data);
      })
      .catch(error => {
        console.log('error');
      })
      .finally(always => {
        console.log('oh well...');
      });
  }
});
