import { useStore } from '~/stores/stores.main'

const connect = () => {
  const SOCKET_URL = "ws://0.0.0.0:1337/ws";

  const store = useStore()

  const socket = new WebSocket(SOCKET_URL);

  socket.onmessage = (event) => {
    console.log("RECEIVE");
    store.$patch({
      data: JSON.parse(event.data)
    })
  };
  socket.onclose = (e) => {
    console.error(e);
    return connect()
  }
}

const getEnum = async () => {
  const API_URL = "http://localhost:1337/enums"

  const store = useStore()

  const res = await fetch(API_URL)

  const { aglomachines } = await res.json()

  store.$patch({
    enum: [...aglomachines]
  })
}

export default async ({ to, from, next, redirect }) => {
  connect()
  await getEnum()
}

