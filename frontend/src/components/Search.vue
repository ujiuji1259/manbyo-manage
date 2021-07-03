<template>
    <div class="row mt-3">
        <div class="col-4 offset-4">
            <input type="text" class="form-control" v-model="search_text">
        </div>
        <div class="col-1">
            <button class="btn btn-primary mb-3" v-on:click="search">search</button>
        </div>
    </div>

    <div class="row mt-3">
        <div class="col-8 offset-2">
            <candidatetable :candidates="candidates" :is_correct="is_correct"
            @change_status_event="change_status"
            @submit_mistake_event="submit_mistake"></candidatetable>
        </div>
    </div>

    <div class="row mt-3" v-if="is_visible_submit_button">
        <div class="col-2 offset-5">
            <button class="btn btn-primary mb-3" v-on:click="search">フィードバック</button>
        </div>
    </div>
</template>

<script>
import candidatetable from '@/components/CandidateTable.vue'
import axios from 'axios' //追記

export default {
    name: "search",
    components: {candidatetable},
    data () {
        return {
            candidates: [],
            is_correct: [],
            search_text: ""
        }
    },
    computed: {
        is_visible_submit_button: function () {
            let feedback_num = this.is_correct.reduce( function (sum, element) {
                return sum + element;
            }, 0);

            return feedback_num > 0;
        }
    },
    watch: {
        candidates: function(newData) {
            this.is_correct = new Array(newData.length).fill(false);
        }
    },
    methods: {
        search() {
            var self = this;
            axios.post('http://localhost:5000/search', {
                name: self.search_text,
            })
            .then(function (response) {
                self.candidates = response.data;
            })
            .catch(function () {
                self.candidates = [];
            })
        },
        submit_mistake(index) {
            axios.post('http://localhost:5000/submit_mistake', {
                name: this.candidates[index]["name"],
            })
            .then(function (response) {
                console.log(response.data);
            })
            .catch( function () {
            })
        },
        change_status(idx) {
            this.is_correct[idx] = !this.is_correct[idx];
        }
    }
}
</script>

<style scoped>

</style>
