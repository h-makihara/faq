<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button class="navbar-toggler navbar-toggler-right"
         type="button"
         data-toggle="collapse"
         data-target="#navbarTogglerDemo02"
         aria-controls="navbarTogglerDemo02"
         aria-expanded="false"
         aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
        </button>

      <a class="navbar-brand" href="#!">FAQ Tools</a>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav mr-auto mt-2 mt-md-0">
          <li class="nav-item active">
            <router-link class="nav-item nav-link" to="/">
              Home
              <span class="sr-only">
                (current)
              </span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-item nav-link" to="/about">About</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-item nav-link" to="/faq">Search</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-item nav-link" to="/faq/create">Create</router-link>
          </li>
        </ul>
      </div>
    </nav>

    </div>
    <router-view/>
  </div>



</template>




<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
