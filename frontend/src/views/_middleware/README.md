# Директория \_middleware

```js
// middleware.js
export default ({ to, from, next, redirect }) => {
  // Some business logic
}

// _routes.js
export default [
  {
    path: '/',
    name: 'Home',
    meta: {
      middleware: [/*<YOUR MIDDLEWARES>*/],
    },
    component: () => import('./view.vue'),
  },
]
```
