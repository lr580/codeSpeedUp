import { createRouter, createWebHistory } from 'vue-router';
const routes = [
    {
        path: '/',
        component: () => import("./components/MainPage.vue")
    },
    {
        path: '/scoreboard',
        component: () => import("./components/ScoreBoard.vue")
    },
    {
        path: '/ide',
        component: () => import("./components/CodeMirrorTester.vue")
    },
    {
        path: '/ide2',
        component: () => import("./components/tester2.vue")
    }
];
const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});
export default router;