<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8">
        <h3 class="has-text-centered">Horarios de los trayectos</h3>
        <div
          v-if="
            horarios.length === 0 ||
            trayectos.length === 0 ||
            buses.length === 0 ||
            rutas.length === 0
          "
        >
          <h3 class="has-text-centered">No hay horarios registrados</h3>
        </div>
        <div v-else>
          <TablaHorarios :data="horarios" />
        </div>
      </div>
      <div class="column is-1">
        <button class="button" @click="setModalState()">Agregar horario</button>
        <AgregarHorarioModal :open="modalState" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'HorarioXTrayecto',
  data() {
    return {
      modalState: false,
    }
  },
  computed: mapState(['horarios', 'trayectos', 'buses', 'rutas']),
  async created() {
    await this.getData({ resource: 'buses' })
    await this.getData({ resource: 'horarios' })
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
