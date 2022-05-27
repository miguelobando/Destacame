<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <th>Terminal</th>
      <th>Ciudad</th>
      <th>Acciones</th>
    </thead>
    <tbody v-for="item in data" :key="item.id">
      <td>{{ item.terminal }}</td>
      <td>{{ item.ciudad }}</td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateRuta(item)">
            Editar
          </button>
          <button
            class="button ml-2 is-danger"
            @click="deleteAndUpdate('rutas', item.id)"
          >
            Borrar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarRutaModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TablaRutas',
  props: {
    data: { type: Array, required: true },
  },
  data() {
    return {
      editable: {},
      modalState: false,
    }
  },
  methods: {
    ...mapActions(['deleteData', 'getData']),
    deleteAndUpdate(resource, key) {
      this.deleteData({ key, resource }).then((e) => {
        this.getData({ resource })
      })
    },
    setModalState() {
      this.modalState = !this.modalState
    },
    updateRuta(item) {
      this.editable = item
      this.setModalState()
    },
  },
}
</script>

<style></style>
