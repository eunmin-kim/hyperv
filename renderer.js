const { ipcRenderer } = require('electron')

const setVB = () => {
    ipcRenderer.send('set-vb','0')
}

const setDocker = () => {
    ipcRenderer.send('set-docker','1')
}

window.onload = function() {
    let status = document.querySelector('.main p')
    ipcRenderer.send('loaded','Success')
    ipcRenderer.on('reply-vb',(evt,data) => {
        if (status.textContent)
        status.classList.remove('docker_mode')
        status.classList.add('vb_mode')
        status.innerText = data
        console.log(data)
    })
    ipcRenderer.on('reply-docker',(evt,data) => {
        if (status.textContent)
        status.classList.remove('vb_mode')
        status.classList.add('docker_mode')
        status.innerText = data
        console.log(data)
    })
}