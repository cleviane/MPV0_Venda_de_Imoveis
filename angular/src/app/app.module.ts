import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GetTodosClientesComponent } from './get-todos-clientes/get-todos-clientes.component';
import { PostClientesComponent } from './post-clientes/post-clientes.component';
import { GetClientesComponent } from './get-clientes/get-clientes.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';


@NgModule({
  declarations: [
    AppComponent,
    GetTodosClientesComponent,
    GetClientesComponent,
    PostClientesComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
