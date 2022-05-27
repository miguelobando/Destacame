<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <tr>
        <th>Placa</th>
        <th>Chofer</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody v-for="data in buses" :key="data.placa">
      <td>{{ data.placa }}</td>
      <td>
        {{ data.chofer === (undefined || null) ? 'Sin Chofer' : data.chofer }}
      </td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateBus(data)">
            Editar
          </button>
          <button
            class="button is-danger ml-2"
            @click="deleteBusAndUpdate('buses', data.placa)"
          >
            Borrar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarBusModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'TablaBuses',
  data() {
    return {
      editable: {},
      modalState: false,
    }
  },
  computed: mapState(['choferes', 'buses']),
  methods: {
    ...mapActions(['deleteData', 'getData']),
    deleteBusAndUpdate(resource, key) {
      this.deleteData({ key, resource }).then((e) => {
        this.getData({ resource })
      })
    },
    updateBus(data) {
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
