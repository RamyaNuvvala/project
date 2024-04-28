const cacheName = 'my-cache';
const filesToCache = [
	'/index.html',
	'/css/style.css',
	'/js/script.js',
	// Add more files as needed
];

self.addEventListener('install', (e) => {
	e.waitUntil(
		caches.open(cacheName).then((cache) => {
			return cache.addAll(filesToCache);
		})
	);
});

self.addEventListener('fetch', (e) => {
	e.respondWith(
		caches.match(e.request).then((response) => {
			return response || fetch(e.request);
		})
	);
});
