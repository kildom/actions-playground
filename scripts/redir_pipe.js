const net = require('net');

const connection_path = '\\\\.\\pipe\\log';

let server = net.createServer()
	.on('error', error => {
		console.error('Server error: ', error);
		process.exit(99);
	})
	.on('listening', () => {
		// Nothing to do here
	})
	.on('connection', socket => {
		socket
			.on('close', hadError => {
				if (hadError) {
					console.error('Server closed with error.');
				}
			})
			.on('data', data => {
				process.stdout.write(data);
			})
			.on('error', error => {
				console.error('Server error: ', error);
				process.exit(99);
			})
			.resume();
	})
	.on('close', () => {
		console.log('Server closed');
	});

server.listen(connection_path);
