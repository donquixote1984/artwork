$(() => {
	$('#render').click(() => {
		$.get('/api/render')
	})
})