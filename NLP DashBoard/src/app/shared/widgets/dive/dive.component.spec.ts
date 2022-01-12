import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DivComponent } from './dive.component';

describe('DivComponent', () => {
  let component: DivComponent;
  let fixture: ComponentFixture<DivComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DivComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DivComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
