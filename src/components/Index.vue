<template>
  <div class="hello">
      <h1>{{ msg }}</h1>
      <b-alert show>Default Alert</b-alert>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      msg:"这里是首页"
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>