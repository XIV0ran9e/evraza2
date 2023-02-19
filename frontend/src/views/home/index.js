import View from './view.vue'
import setSocket from '~/views/_middleware/set-socket.js'

export default [
  {
    path: '/',
    name: 'Home',
    component: View,
    meta: {
      middlewares: [setSocket],
    },
  },
]
