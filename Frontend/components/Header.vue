<template>
  <header :class="{ 'is-transformed': !showNavbar }" class="navbar">
    <div class="container">
      <div class="navbar-brand is-family-secondary">
        <nuxt-link to="/" class="navbar-item">
          <h1 class="is-size-4">Destacame</h1>
        </nuxt-link>
        <a
          :aria-expanded="isActive"
          :class="{ 'is-active': isActive }"
          role="button"
          class="navbar-burger"
          aria-label="menu"
          data-target="collapse"
          @click="isActive = !isActive"
        >
          <span aria-hidden="true" />
          <span aria-hidden="true" />
          <span aria-hidden="true" />
        </a>
      </div>
      <div
        id="collapse"
        :class="{ 'is-active': isActive }"
        class="navbar-menu is-paddingless"
      >
        <nav class="navbar-end">
          <NuxtLink to="/buses">
            <a class="navbar-item"> Buses </a>
          </NuxtLink>
          <NuxtLink to="/choferes">
            <a class="navbar-item"> Choferes </a>
          </NuxtLink>
          <NuxtLink to="/rutas">
            <a class="navbar-item"> Rutas </a>
          </NuxtLink>
          <NuxtLink to="/trayectos">
            <a class="navbar-item"> Trayectos </a>
          </NuxtLink>
          <NuxtLink to="/horarioxtrayecto">
            <a class="navbar-item"> Horarios de trayecto </a>
          </NuxtLink>
          <NuxtLink to="/boletos">
            <a class="navbar-item"> Boletos </a>
          </NuxtLink>
          <NuxtLink to="/pasajeros">
            <a class="navbar-item"> Pasajeros </a>
          </NuxtLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<script>
import throttle from 'lodash/throttle'

export default {
  name: 'Header',
  data() {
    return {
      isActive: false,
      showNavbar: true,
    }
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', throttle(this.closeMenu, 500))
      window.addEventListener('scroll', throttle(this.hideNav, 250))
    })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.closeMenu)
    window.removeEventListener('scroll', this.hideNav)
  },
  methods: {
    closeMenu() {
      this.isActive = false
    },
    hideNav() {
      const currentScrollPosition =
        window.pageYOffset || document.documentElement.scrollTop
      if (currentScrollPosition < 0) return
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) return
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      this.lastScrollPosition = currentScrollPosition
      setTimeout(this.closeMenu, 250)
    },
  },
}
</script>

<style></style>
