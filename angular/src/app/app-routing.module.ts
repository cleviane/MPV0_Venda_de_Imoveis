import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetTodosClientesComponent } from './get-todos-clientes/get-todos-clientes.component';
import { GetClientesComponent } from './get-clientes/get-clientes.component';
import { PostClientesComponent } from './post-clientes/post-clientes.component';

const routes: Routes = [
  {path:'gettodosclientes', component: GetTodosClientesComponent},
  {path:'addcliente', component: PostClientesComponent},
  {path:'getclienteid', component: GetClientesComponent}

]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
