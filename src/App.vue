<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png">
    <br>
    <img class="logo" src="./assets/dj.png">
    <p>
      Welcome to your Django - Vue.js app!
    </p>

    <ul class="nav nav-tabs">
      <li><router-link to="/index">首页</router-link>  <!--用于点击查看组件--></li>
      <li><router-link to="/micro">学位课</router-link>  <!--用于点击查看组件--></li>
      <li><router-link to="/course">课程</router-link></li>  <!--用于点击查看组件-->
      <li><router-link to="/news">深科技</router-link></li>  <!--用于点击查看组件-->
      <!--如果已经登录了，就不用在登录了，在页面还是显示当前用户和注销，如果没有登录就显示登录-->
      <li v-if="this.$store.state.username">
        <span><a>欢迎{{ this.$store.state.username }}登录</a></span>
        <span><a @click="logout()">注销</a></span>
      </li>
      <li v-else=""> <router-link to="/login">登录</router-link></li>
    </ul>
   <router-view/>  <!--组件显示的位置-->

  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    logout () {
    this.$store.commit('clearToken');
    }
  }
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>
