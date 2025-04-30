import { defineStore } from 'pinia'

function pushLink(label, route){
    return {'label': label, 'route': route};
}

export const useLinksStore = defineStore('linksStore', {
    state: () => {
        let init = []
        init.push(pushLink('Home', '/'));
        init.push(pushLink('About', '/about'));
        return { links: init, init: init };
    },
    actions: {
        updateLinks(isUserAuthenticated) {
            this.links = [...this.init]; // copy the content of this.init in this.links : reinitialize links
            if(isUserAuthenticated) {
                this.links.push(pushLink('Dashboard', '/dashboard'));
                this.links.push(pushLink('Manage', '/manage'));
                this.links.push(pushLink('Logout', '/logout'));
            }else{
                this.links.push(pushLink('Login', '/login'));
                this.links.push(pushLink('Register', '/register'));
            }
        },
    },
})