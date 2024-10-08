let currentPage = 1;
const postsPerPage = 4; 
const posts = document.querySelectorAll('.blog-post'); // 所有的文章元素
const totalPosts = posts.length;
const totalPages = Math.ceil(totalPosts / postsPerPage);
function showPage(page) {
    currentPage = page;
    posts.forEach((post, index) => {
        post.style.display = 'none';
    });
    const start = (currentPage - 1) * postsPerPage;
    const end = start + postsPerPage;
    for (let i = start; i < end && i < totalPosts; i++) {
        posts[i].style.display = 'block';
    }
    updatePagination();
}
function updatePagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = ''; 
    //const prevBtn = document.createElement('button');
    //prevBtn.textContent = 'Previous';
    //prevBtn.disabled = currentPage === 1;
    //prevBtn.onclick = () => showPage(currentPage - 1);
    //pagination.appendChild(prevBtn);
    for (let i = 1; i <= totalPages; i++) {
        const pageBtn = document.createElement('button');
        pageBtn.textContent = i;
        if (i === currentPage) {
            pageBtn.style.fontWeight = 'bold'; // 当前页加粗
        }
        pageBtn.onclick = () => showPage(i);
        pagination.appendChild(pageBtn);
    }
    //const nextBtn = document.createElement('button');
    //nextBtn.textContent = 'Next';
    //nextBtn.disabled = currentPage === totalPages;
    //nextBtn.onclick = () => showPage(currentPage + 1);
    //pagination.appendChild(nextBtn);
}
document.addEventListener("DOMContentLoaded", function() {
    showPage(1);
});
