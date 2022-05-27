<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Trayectos</h3>
        <div v-if="trayectos.length === 0 || rutas.length === 0">
          <h3 class="has-text-centered">No hay trayectos registrados</h3>
        </div>
        <div v-else>
          <TablaTrayectos :data="trayectos" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">
          Agregar trayectos
        </button>
        <AgregarTrayectoModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Trayectos',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['trayectos', 'rutas']),
  async created() {
    await this.getData({ resource: 'horarios' })
    await this.getData({ resource: 'boletos' })
    await this.getData({ resource: 'rutas' })
    await this.getData({ resource: 'trayectos' })
  },
  methods: {
    ...mapActions(['getData']),
    setModalState() {
      this.modalState = !this.modalState
    },
  },
}
</script>

<style></style>
