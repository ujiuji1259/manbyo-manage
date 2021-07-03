<template>
    <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">順位</th>
                <th scope="col">病名</th>
                <th scope="col">標準病名</th>
                <th scope="col">ICDコード</th>
                <th scope="col">ラベル</th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="(m, index) in candidates" :key="index">
                <th scope="row">{{index+1}}</th>
                <td><a href="#" v-on:click.prevent="submit_mistake(index)">{{m.name}}</a></td>
                <td>{{m.norm}}</td>
                <td>{{m.icd}}</td>
                <td>
                    <button type="button" class="btn" v-bind:class="is_correct[index] ? 'btn-danger' : 'btn-light'"
                    v-on:click="change_status(index)" v-if="!has_same_data">
                    {{is_correct[index] ? "correct" : ""}}
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>

export default {
    name: "candidatetable",
    props: {
        candidates: Object,
        is_correct: Object
    },
    methods: {
        change_status(idx) {
            this.$emit('change_status_event', idx);
        },
        submit_mistake(idx) {
            this.$emit('submit_mistake_event', idx);
        }
    }
}
</script>

<style scoped>

</style>
