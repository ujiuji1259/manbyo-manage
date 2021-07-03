<template>
    <nav class="navbar navbar-expand-lg navbar-dark header">
        <div class="container-fluid">
            <router-link to="/">
                <img src="@/assets/sociocom.png"  alt="" height="50" class="d-inline-block align-top">
            </router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse ml-5" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/about" exact exact-active-class="active">About</router-link>
                    </li>

                    <li class="nav-item ml-3">
                        <router-link to="/" exact exact-active-class="active">検索</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<style scoped>
.header {
    background: #00B295;
    padding: 10px 0px;
    color: white;
    font-size: 1.5em;
}
a {
    color: white;
    font-weight: bold;
}
a:hover {
    color: #b7dbf2;
    text-decoration: underline;
}
</style>
