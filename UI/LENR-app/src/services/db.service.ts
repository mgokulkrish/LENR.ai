import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { APP_CONSTANTS } from '../constants/app.constants';

@Injectable({
    providedIn: 'root',
})
export class DBService {
    constructor(private http: HttpClient) { }

    public getDocs(question: string): Observable<any> {
        const url = APP_CONSTANTS.dbServer + '/prompt';

        return this.http.post(url, { question: question });
    }
}