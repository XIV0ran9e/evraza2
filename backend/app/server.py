import uvicorn

if __name__ == '__main__':
    uvicorn.run('asgi:app', host='0.0.0.0', port=1337, reload=True)
