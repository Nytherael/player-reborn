document.addEventListener("DOMContentLoaded", function () {
  fetch("https://api.allorigins.win/raw?url=https://discord.com/api/guilds/1330977532824129616/widget.json")
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("online-count").textContent =
        "Online Members: " + data.presence_count;
    })
    .catch(() => {
      document.getElementById("online-count").textContent =
        "Unable to load player count";
    });
});