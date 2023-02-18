class MiddlewareSupport {
  constructor(router) {
    this.router = router
  }
  async hook(to, from, next) {
    let redirected = false
    const { middlewares = [] } = to.meta
    for (const middleware of middlewares) {
      const result_pipeline = await middleware({
        to,
        from,
        next: (name) => {
          redirected = true
          next({ name })
        },
        force_redirect: (url) => (window.location = url),
        redirect: (url) => this.router.push(url),
      })
      if (result_pipeline === false) break
    }
    if (!redirected) next()
  }
}

export function hook(router) {
  const middleware = new MiddlewareSupport(router)
  router.beforeEach(async (to, from, next) => {
    if (!to.meta.middleware) return next()
    await middleware.hook(to, from, next)
  })
}
