import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SementicComponent } from './sementic.component';

describe('SementicComponent', () => {
  let component: SementicComponent ;
  let fixture: ComponentFixture<SementicComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SementicComponent  ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SementicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
