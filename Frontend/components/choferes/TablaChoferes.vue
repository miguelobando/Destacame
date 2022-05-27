<template>
  <table class="table is-hoverable is-fullwidth">
    <thead>
      <th>Nombre</th>
      <th>Apellido</th>
      <th>Email</th>
      <th>Acciones</th>
    </thead>
    <tbody v-for="item in data" :key="item.email">
      <td>{{ item.nombre }}</td>
      <td>{{ item.apellido }}</td>
      <td>{{ item.email }}</td>
      <td>
        <div class="is-flex">
          <button class="button is-success" @click="updateChofer(item)">
            Editar
          </button>
          <button
            class="button ml-2 is-danger"
            @click="deleteAndUpdate(item.email, 'choferes')"
          >
            Borar
          </button>
        </div>
      </td>
    </tbody>
    <ModificarChoferModal :open="modalState" :current="editable" />
  </table>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TablaChoferes',
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
    deleteAndUpdate(key, resource) {
      this.deleteData({ key, resource }).then((e) => {
        this.getData({ resource })
      })
    },
    updateChofer(data) {
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
