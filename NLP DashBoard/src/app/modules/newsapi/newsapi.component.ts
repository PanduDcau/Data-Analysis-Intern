import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-newsapi',
  templateUrl: './newsapi.component.html',
  styleUrls: ['./newsapi.component.scss']
})
export class NewsapiComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  toppings = new FormControl();
  verbs = new FormControl();

  toppingList: string[] = ['Social', 'Crime', 'Sport', 'Entertainment', 'Political', 'Youth'];
  verbList: string[] = ['Continous' ,'Past' , 'Present' , 'Future'];

}
