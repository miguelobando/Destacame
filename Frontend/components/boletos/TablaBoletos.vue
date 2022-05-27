<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <th>Pasajero</th>
      <th>Trayecto</th>
      <th>Horario</th>
      <th>Bus</th>
      <th>Asiento</th>
      <th>Acciones</th>
    </thead>
    <tbody v-for="item in data" :key="item.id">
      <td class="is-size-7">{{ item.pasajero }}</td>
      <td class="is-size-7">{{ showDetalleTrayecto(item.trayecto) }}</td>
      <td class="is-size-7">{{ showHorario(item.horario) }}</td>
      <td class="is-size-7">{{ showBus(item.asiento) }}</td>
      <td class="is-size-7">{{ showNumeroAsiento(item.asiento) }}</td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateBoletos(item)">
            Editar
          </button>
          <button
            class="button ml-2 is-danger"
            @click="deleteTrayectoAndUpdate('boletos', item.id)"
          >
            Borar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarBoletosModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'TablaBoletos',
  props: {
    data: { type: Array, required: true },
  },
  data() {
    return {
      editable: {},
      modalState: false,
    }
  },
  computed: mapState([
    'asientos',
    'trayectos',
    'rutas',
    'pasajeros',
    'horarios',
  ]),
  methods: {
    ...mapActions(['getData', 'deleteData']),
    showDetalleTrayecto(id) {
      const trayecto = this.trayectos.find((e) => e.id === id)
      const inicio = this.rutas.find((e) => e.id === trayecto.inicio)
      const fin = this.rutas.find((e) => e.id === trayecto.fin)
      return `De: ${inicio.terminal}, ${inicio.ciudad}. Hasta  ${fin.terminal}, ${fin.ciudad}`
    },
    showHorario(id) {
      const item = this.horarios.find((e) => e.id === id)
      const newdate = new Date(item.horario).toLocaleDateString('es-cl')
      const newhour = new Date(item.horario)
        .toLocaleTimeString('es-cl')
        .slice(0, -3)
      return `${newdate} ${newhour}`
    },
    showNumeroAsiento(id) {
      const asiento = this.asientos.find((e) => e.id === id)
      return asiento?.numeroAsiento
    },
    deleteTrayectoAndUpdate(resource, key) {
      this.deleteData({ resource, key }).then((e) => {
        this.getData({ resource })
      })
    },
    showBus(id) {
      const asiento = this.asientos.find((e) => e.id === id)

      return asiento?.bus
    },
    setModalState() {
      this.modalState = !this.modalState
    },
    updateBoletos(data) {
      this.editable = data
      this.setModalState()
    },
  },
}
</script>

<style></style>
