import { HttpClient } from '@angular/common/http';
import { Injectable, NgZone } from '@angular/core';
import { Observable, concatAll, delay, from, map, of } from 'rxjs';
import { APP_CONSTANTS } from '../constants/app.constants';

@Injectable({
  providedIn: 'root',
})
export class LlmService {
  constructor(private http: HttpClient, private zone: NgZone) {}
}