import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root',
})
export class UtilsService {
    constructor() { }

    public processStreamData(stream: string) {
        const str = stream.replace(/(?:\r\n|\r|\n)/g, '</br>');
        const fixedData = str.trim();
        console.log(fixedData);
        return fixedData;
    }
}