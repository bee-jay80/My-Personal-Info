document.addEventListener('DOMContentLoaded', function(){
	const form = document.getElementById('pw-form');
	const loading = document.getElementById('loading-overlay');
	if(form){
		form.addEventListener('submit', function(e){
			// prevent double submits
			if (form.dataset.submitted === '1') {
				e.preventDefault();
				return;
			}
			form.dataset.submitted = '1';

			// show loading overlay to indicate work
			loading.classList.remove('hidden');
			// also ensure inline display is set (works if CSS hasn't loaded)
			loading.style.display = 'flex';
			// disable only submit buttons to avoid double submit, keep hidden inputs (csrf) enabled
			Array.from(form.querySelectorAll('button, input[type=submit]')).forEach(el=>el.disabled=true);
		});
	}

	// small touch: focus password input if present
	const pw = document.getElementById('password');
	if(pw){
		pw.focus();
	}
});
