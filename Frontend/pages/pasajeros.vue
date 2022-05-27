<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Pasajeros</h3>
        <div v-if="pasajeros.length === 0">
          <h3 class="has-text-centered">No hay pasajeros registrados</h3>
        </div>
        <div v-else>
          <TablaPasajeros :data="pasajeros" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">
          Agregar pasajero
        </button>
        <AgregarPasajeroModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'PasajerosPage',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['pasajeros']),
  created() {
    this.getData({ resource: 'pasajeros' })
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
