<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <th>Trayecto</th>
      <th>Bus</th>
      <th>Horario</th>
      <th>Acciones</th>
    </thead>
    <tbody v-for="item in data" :key="item.id">
      <td>{{ showTrayecto(item.trayecto) }}</td>
      <td>{{ item.bus }}</td>
      <td>{{ showLocalTime(item.horario) }}</td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateHorario(item)">
            Editar
          </button>

          <button
            class="button ml-2 is-danger"
            @click="deleteHorarioAndUpdate('horarios', item.id)"
          >
            Borar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarHorarioModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'TablaHorarios',
  props: {
    data: { type: Array, required: true },
  },
  data() {
    return {
      editable: {},
      modalState: false,
    }
  },
  computed: mapState(['rutas', 'trayectos']),
  methods: {
    ...mapActions(['deleteData', 'getData']),
    deleteHorarioAndUpdate(resource, key) {
      this.deleteData({ resource, key }).then((e) => {
        this.getData({ resource })
      })
    },
    showTrayecto(id) {
      const trayecto = this.trayectos.find((e) => e.id === id)
      const inicio = this.rutas.find((e) => e.id === trayecto.inicio)
      const fin = this.rutas.find((e) => e.id === trayecto.fin)
      return `Desde: ${inicio.terminal}, ${inicio.ciudad}. Hasta:  ${fin.terminal}, ${fin.ciudad}`
    },
    showLocalTime(time) {
      const newdate = new Date(time).toLocaleDateString('es-cl')
      const newhour = new Date(time).toLocaleTimeString('es-cl').slice(0, -3)
      return `${newdate} ${newhour}`
    },
    updateHorario(data) {
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
