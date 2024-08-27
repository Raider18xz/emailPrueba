document.querySelector('form')
    .addEventListener('submit', e => {
        e.preventDefault();  // Previene el comportamiento predeterminado del formulario
        
        // Crear un objeto FormData con los datos del formulario
        const formData = new FormData(e.target);
        
        // Convertir FormData a un objeto plain
        const data = Object.fromEntries(formData.entries());
        
        // Enviar los datos al backend usando fetch
        fetch('http://localhost:5000/email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Especificar el tipo de contenido
            },
            body: JSON.stringify(data)  // Convertir el objeto data a JSON
        })
        .then(response => response.json())  // Analizar la respuesta del servidor como JSON
        .then(data => {
            console.log('Success:', data);  // Manejar la respuesta exitosa
            alert('Correo enviado exitosamente');
        })
        .catch((error) => {
            console.error('Error:', error);  // Manejar errores
            alert('Error al enviar el correo');
        });
    });
