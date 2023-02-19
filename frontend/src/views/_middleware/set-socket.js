import { useStore } from '~/stores/stores.main'

const connect = async () => {
  const SOCKET_URL = "ws://0.0.0.0:1337/ws";
  const API_URL = "http://localhost:1337/getlast"

  const store = useStore()

  const socket = new WebSocket(SOCKET_URL);


  const res = await fetch(API_URL)

  const data = await res.json()

  console.log(data);
  // store.$patch({
  //     data: JSON.parse(event.data)
  //   })
  store.$patch({
      data: {...data}
    })
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
  getEnum()
}

