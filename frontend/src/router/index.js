import Vue from 'vue';
import Router from 'vue-router';
import SignUp from '@/components/SignUp.vue';
import CompanyRegistration from '@/components/CompanyRegistration.vue';
import ModuleSettings from '@/components/ModuleSettings.vue';
import ProcessDesign from '@/components/ProcessDesign.vue';
import FormCreation from '@/components/FormCreation.vue';
import WorkflowManagement from '@/components/WorkflowManagement.vue';
import Dashboard from '@/components/Dashboard.vue';
import ModulePublication from '@/components/ModulePublication.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/company-registration',
      name: 'CompanyRegistration',
      component: CompanyRegistration
    },
    {
      path: '/module-settings',
      name: 'ModuleSettings',
      component: ModuleSettings
    },
    {
      path: '/process-design',
      name: 'ProcessDesign',
      component: ProcessDesign
    },
    {
      path: '/form-creation',
      name: 'FormCreation',
      component: FormCreation
    },
    {
      path: '/workflow-management',
      name: 'WorkflowManagement',
      component: WorkflowManagement
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/module-publication',
      name: 'ModulePublication',
      component: ModulePublication
    }
  ]
});