const { app, BrowserWindow, ipcMain } = require("electron");
const { resolve } = require("path");
require('dotenv').config();

const createWindow = () => {
  const win = new BrowserWindow({
    width: 600,
    height: 200,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
    // autoHideMenuBar: true,
  });

  win.loadFile("index.html");
  ipcMain.on("loaded", (evt, data) => {});

  ipcMain.on("set-vb", async (evt, data) => {
    // var py = require("child_process").execFile("./dist/set.exe", [data]);
    result = await python(data)
    evt.reply("reply-vb",result)
  });

  ipcMain.on("set-docker", async (evt, data) => {
    result = await python(data)
    evt.reply("reply-docker",result)
    // var py = require("child_process").execFile("./dist/set.exe",[data])
  });
};

app.whenReady().then(() => {
  createWindow();
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

const python = (input) => {
  return new Promise((resolve, reject) => {
    // var py = require("child_process").execFile("./dist/set.exe", [input]);
    var py = require("child_process").spawn("python", ["./py/set.py", input]);
    var result;
    py.stdout.on("data", (data) => {
      result = data.toString('utf8')
      resolve(result);
    });
  });
};
