module.exports = {
  apps: [
    {
      name: "liveuta-scheduler",
      interpreter: "./.venv/bin/python",
      script: "./src/main.py",
      args: "",
      watch: false, // dev
      autorestart: true,
    },
  ],
};
