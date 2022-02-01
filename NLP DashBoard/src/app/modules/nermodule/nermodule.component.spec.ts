import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NermoduleComponent } from './nermodule.component';

describe('NermoduleComponent', () => {
  let component: NermoduleComponent;
  let fixture: ComponentFixture<NermoduleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NermoduleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NermoduleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
