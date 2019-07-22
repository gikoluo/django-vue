<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png">
    <br>
    <img class="logo" src="./assets/dj.png">
    <p>
      Welcome to your Django - Vue.js app!
    </p>

    <div>
      <b-nav>
        <b-nav-item active><router-link to="/index">首页</router-link></b-nav-item>
        <b-nav-item><router-link to="/micro">学位课</router-link></b-nav-item>
        <b-nav-item><router-link to="/course">课程</router-link></li></b-nav-item>
        <b-nav-item><router-link to="/news">深科技</router-link></li></b-nav-item>
        <b-nav-item-dropdown
          v-if="this.$store.state.username"
          id="my-nav-dropdown"
          text="Dropdown"
          toggle-class="nav-link-custom"
          right
        >
          <b-dropdown-item>欢迎</b-dropdown-item>
          <b-dropdown-item><a @click="logout()">注销</a></b-dropdown-item>
          
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item>three</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item v-else=""><router-link to="/login">登录</router-link></b-nav-item>
      </b-nav>
    </div>
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
