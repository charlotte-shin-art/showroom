document.addEventListener('DOMContentLoaded', () => {
    const galleryContainer = document.getElementById('gallery-container');
    const modal = document.getElementById('lightbox-modal');
    const modalClose = document.getElementById('modal-close');
    
    // Modal Details Elements
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalCategory = document.getElementById('modal-category');
    const modalDesc = document.getElementById('modal-desc');
    const modalLink = document.getElementById('modal-link');

    // Read Global Gallery Data (Loaded from gallery_data.js)
    if (window.galleryData && window.galleryData.length > 0) {
        renderGallery(window.galleryData);
    } else {
        console.error("No gallery data found.");
        galleryContainer.innerHTML = '<p style="text-align:center;width:100%;color:#888;">No artworks found yet. Run the update script.</p>';
    }

    // Render Gallery
    function renderGallery(data) {
        galleryContainer.innerHTML = '';
        data.forEach(item => {
            const div = document.createElement('div');
            div.className = 'gallery-item';
            div.dataset.id = item.id;
            
            // Use thumbnail for the masonry grid if available, otherwise fallback to original src
            const thumbSrc = item.thumb_src ? item.thumb_src : item.src;
            
            div.innerHTML = `
                <img src="${thumbSrc}" alt="${item.title}" onerror="this.src='${item.fallback_src || 'https://via.placeholder.com/800/eeeeee/888?text=Image+Missing'}'" loading="lazy">
                <div class="gallery-overlay">
                    <h3 class="item-title">${item.title}</h3>
                    <p class="item-desc">${item.category || 'Artwork'}</p>
                </div>
            `;
            
            div.addEventListener('click', () => openModal(item));
            galleryContainer.appendChild(div);
        });
    }

    // Modal Functions
    function openModal(item) {
        modalImg.src = item.src;
        // fallback in case local image fails in browser due to CORS or path issues
        modalImg.onerror = function() { this.src = item.fallback_src; }; 
        modalTitle.textContent = item.title;
        if(modalCategory) modalCategory.textContent = item.category || 'Artwork';
        modalDesc.innerHTML = item.desc.replace(/\n/g, '<br>');
        modalLink.href = item.link;
        
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    modalClose.addEventListener('click', closeModal);
    
    // Close modal when clicking outside of the content
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });

    // Author Profile Modal Logic
    const authorAvatar = document.getElementById('author-avatar');
    const authorModal = document.getElementById('author-modal');
    const authorModalCloseBtn = document.querySelector('.author-modal-close');

    if (authorAvatar && authorModal && authorModalCloseBtn) {
        authorAvatar.addEventListener('click', () => {
            authorModal.classList.add('show');
            document.body.style.overflow = 'hidden';
        });

        authorModalCloseBtn.addEventListener('click', () => {
            authorModal.classList.remove('show');
            document.body.style.overflow = 'auto';
        });

        authorModal.addEventListener('click', (e) => {
            if (e.target === authorModal) {
                authorModal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        });
    }

});
