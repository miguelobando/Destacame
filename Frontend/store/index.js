const baseUrl = 'http://127.0.0.1:8000/api/v1'

export const state = () => ({
  buses: [],
  choferes: [],
  rutas: [],
  trayectos: [],
  horarios: [],
  boletos: [],
  pasajeros: [],
  asientos: [],
})

export const mutations = {
  setData(state, payload) {
    state[payload.state] = payload.data
  },
}

export const actions = {
  // #region generico
  async getData({ commit }, payload) {
    const data = (await this.$axios.get(`${baseUrl}/${payload.resource}/`)).data
    const content = {
      data,
      state: payload.resource,
    }
    commit('setData', content)
    return data
  },

  async addData(commit, payload) {
    let result = 0
    try {
      result = (
        await this.$axios.post(`${baseUrl}/${payload.resource}/`, {
          ...payload.data,
        })
      ).status
    } catch (error) {
      result = 400
    }
    return result
  },

  async deleteData(commit, payload) {
    const result = await this.$axios.delete(
      `${baseUrl}/${payload.resource}/${payload.key}/`
    )
    return result
  },

  async updateData(commit, payload) {
    let result
    try {
      result = (
        await this.$axios.put(
          `${baseUrl}/${payload.resource}/${payload.key}/`,
          {
            ...payload.data,
          }
        )
      ).status
    } catch (error) {
      result = 404
    }
    return result
  },
}
