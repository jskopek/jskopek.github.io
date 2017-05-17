/* pick a random background from list of options */
var backgrounds = [
    { 'id': 'london-city-center', 'source': 'City Center, London' },
    { 'id': 'eiffel-tower', 'source': 'Eiffel Tower, Paris' },
    { 'id': 'samuel-beckett-bridge', 'source': 'Samuel Beckett Bridge, Ireland' },
];
var index = Math.floor(Math.random() * backgrounds.length);
var background = backgrounds[index];
document.getElementById('background-video').style.backgroundImage = "url(/assets/" + background.id + ".jpg)";
document.getElementById('background-video').src = "/assets/" + background.id + ".mp4";
document.getElementById('background-video-source').textContent = background.source;

