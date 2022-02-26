const { ipcRenderer } = require('electron')

const setVB = () => {
    ipcRenderer.send('set-vb','0')
}

const setDocker = () => {
    ipcRenderer.send('set-docker','1')
}
window.onload = function() {
    ipcRenderer.send('loaded','Success')
    ipcRenderer.on('reply-vb',(evt,data) => {
        alert(data)
        document.querySelector('.vb_mode p').innerText = data
        console.log(data)
    })
    ipcRenderer.on('reply-docker',(evt,data) => {
        document.querySelector('.docker_mode p').innerText = data
        console.log(data)
    })
}