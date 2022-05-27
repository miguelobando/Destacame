<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Boletos</h3>
        <div
          v-if="
            boletos.length === 0 || trayectos.length === 0 || rutas.length === 0
          "
        >
          <h3 class="has-text-centered">No hay boletos registrados</h3>
        </div>
        <div v-else>
          <TablaBoletos :data="boletos" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">Vender Boletos</button>
        <AgregarBoletosModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'BoletosPage',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState([
    'boletos',
    'trayectos',
    'rutas',
    'asientos',
    'pasajeros',
  ]),
  async created() {
    await this.getData({ resource: 'asientos' })
    await this.getData({ resource: 'horarios' })
    await this.getData({ resource: 'pasajeros' })
    await this.getData({ resource: 'trayectos' })
    await this.getData({ resource: 'rutas' })
    await this.getData({ resource: 'boletos' })
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
