<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <th>Origen</th>
      <th>Destino</th>
      <th>Promedio de pasajeros</th>
      <th>Acciones</th>
    </thead>
    <tbody v-for="item in data" :key="item.id">
      <td>{{ getNombreRuta(item.inicio) }}</td>
      <td>{{ getNombreRuta(item.fin) }}</td>
      <td><PromedioPasajeros :id="item.id" /></td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateTrayecto(item)">
            Editar
          </button>
          <button
            class="button ml-2 is-danger"
            @click="deleteTrayectoAndUpdate('trayectos', item.id)"
          >
            Borar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarTrayectoModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'TablaTrayectos',

  props: {
    data: { type: Array, required: true },
  },
  data() {
    return {
      editable: {},
      modalState: false,
    }
  },
  computed: mapState(['rutas', 'buses', 'horarios', 'boletos']),
  methods: {
    ...mapActions(['getData', 'deleteData']),
    deleteTrayectoAndUpdate(resource, key) {
      this.deleteData({ resource, key }).then((e) => {
        this.getData({ resource })
      })
    },
    getNombreRuta(id) {
      const ruta = this.rutas.find((e) => e.id === id)
      return `${ruta.terminal}, ${ruta.ciudad}`
    },
    updateTrayecto(data) {
      this.editable = data
      this.setModalState()
    },
    setModalState() {
      this.modalState = !this.modalState
    },
  },
}
</script>

<style></style>
