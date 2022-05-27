<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Rutas</h3>
        <div v-if="rutas.length === 0">
          <h3 class="has-text-centered">No hay rutas registradas</h3>
        </div>
        <div v-else>
          <TablaRutas :data="rutas" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">Agregar Ruta</button>
        <AgregarRutaModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'RutasPage',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['rutas']),
  created() {
    this.getData({ resource: 'rutas' })
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
