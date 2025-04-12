<template>
  <v-container class="pa-md-12">
    <router-view></router-view>
  </v-container>
</template>


<style>
@import './style.css';
#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0rem;
  font-weight: normal;
}

@media (min-width: 1024px) {
  #app {
    padding: 0 2rem;
  }
}

.dialog-footer {
  text-align: center;
}

.dialog-footer button {
  width: 100px;
  margin: 0 0 10px 0;
}

@media (min-width: 1024px) {
  .dialog-footer button{
    width: 100px;
    margin: 0 10px 0 0;
  }
}
</style>
