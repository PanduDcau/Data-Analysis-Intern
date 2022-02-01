import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DefaultComponent } from './layouts/default/default.component';
import { DashboardComponent } from './modules/dashboard/dashboard.component';
import { PostsComponent } from './modules/posts/posts.component';
import { SementicComponent } from './modules/sementic/sementic.component';
import { NermoduleComponent } from './modules/nermodule/nermodule.component';
import { NewsapiComponent } from './modules/newsapi/newsapi.component';

const routes: Routes = [{
  path: '',
  component: DefaultComponent,
  children: [{
    path: '',
    component: DashboardComponent
  }, {
    path: 'posts',
    component: PostsComponent
  },
  {
    path: 'sementic',
    component: SementicComponent
  },
  {
    path: 'nermod',
    component: NermoduleComponent
  },
  {
    path: 'newsapi',
    component: NewsapiComponent
  }
  ]
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
