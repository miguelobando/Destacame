<template>
  <div>
    <Header />
    <div class="columns is-centered">
      <div class="column is-8 mt-4">
        <div>
          <div class="columns">
            <div class="column is-6" style="width: auto">
              <h3 class="is-inline-block">Buses de</h3>
              <div class="select is-inline-block">
                <select v-model="trayecto" @change="executeQuery">
                  <option value="">Trayecto</option>
                  <option
                    v-for="item in trayectos"
                    :key="item.id"
                    :value="item.id"
                  >
                    {{ getNombreRuta(item.inicio) }} a
                    {{ getNombreRuta(item.fin) }}
                  </option>
                </select>
              </div>
            </div>
            <div class="column is-8">
              <h3 class="is-inline-block">con más de</h3>
              <div class="select is-inline-block">
                <select v-model="capacidad" @change="executeQuery">
                  <option value="">Capacidad</option>
                  <option v-for="n in 10" :key="n" :value="n">
                    {{ n * 10 }} %
                  </option>
                </select>
              </div>
              <h3 class="is-inline-block">de capacidad vendida</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="filtered.length > 0" class="columns is-centered">
      <div class="column is-8">
        <table class="table is-hoverable is-fullwidth">
          <thead>
            <th>Trayecto</th>
            <th>Bus</th>
            <th>Horario</th>
          </thead>
          <tbody v-for="item in filtered" :key="item.id">
            <td>{{ showTrayecto(item.trayecto) }}</td>
            <td>{{ item.bus }}</td>
            <td>{{ showLocalTime(item.horario) }}</td>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'IndexPage',
  data() {
    return {
      capacidad: '',
      trayecto: '',
      filtered: [],
    }
  },
  computed: mapState(['rutas', 'trayectos', 'horarios', 'boletos']),
  async created() {
    if (this.rutas.length === 0) await this.getData({ resource: 'rutas' })
    if (this.trayectos.length === 0)
      await this.getData({ resource: 'trayectos' })
    if (this.horarios.length === 0) await this.getData({ resource: 'horarios' })
    if (this.boletos.length === 0) await this.getData({ resource: 'boletos' })
  },

  methods: {
    ...mapActions(['getData']),
    getNombreRuta(id) {
      const ruta = this.rutas.find((e) => e.id === id)
      return `${ruta.terminal}, ${ruta.ciudad}`
    },
    executeQuery() {
      if (this.trayecto !== '' && this.capacidad !== '') {
        this.$axios
          .get(
            `http://127.0.0.1:8000/api/v1/trayectos/${this.trayecto}/capacidad/${this.capacidad}/`
          )
          .then((e) => {
            this.filtered = e.data
          })
      }
    },
    showTrayecto(id) {
      const trayecto = this.trayectos.find((e) => e.id === id)
      const inicio = this.rutas.find((e) => e.id === trayecto.inicio)
      const fin = this.rutas.find((e) => e.id === trayecto.fin)
      return `Desde: ${inicio.terminal}, ${inicio.ciudad}. Hasta:  ${fin.terminal}, ${fin.ciudad}`
    },
    showLocalTime(time) {
      const newdate = new Date(time).toLocaleDateString('es-cl')
      const newhour = new Date(time).toLocaleTimeString('es-cl')
      return `${newdate} ${newhour}`
    },
  },
}
</script>
