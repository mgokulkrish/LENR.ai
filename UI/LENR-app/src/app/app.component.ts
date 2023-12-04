import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { APP_CONSTANTS } from '../constants/app.constants';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  public title: string = 'LENR AI';
  public streamText: string = '';
  public promptText: string = '';
  public theme = APP_CONSTANTS.lightTheme;

  public isFetching: boolean = false;

  constructor() { }

  getAnswer(): void {
    console.log('Get Answer for --> ', this.promptText);
    this.isFetching = !this.isFetching;
    this.streamText = '';
    this.getStream();
  }

  private async getStream() {
    let response = await fetch(APP_CONSTANTS.cppServer + "/completion", {
      method: 'POST',
      body: JSON.stringify({
        prompt: this.promptText,
        n_predict: 1024,
        stream: true,
      })
    });

    const reader = response.body?.pipeThrough(new TextDecoderStream()).getReader();

    while (true) {
      const data = await reader?.read();

      let lastLine = data?.value?.split(/\r?\n/);
      let last_array = lastLine?.filter(e => e != '');

      let stop = false;
      last_array?.forEach((str) => {
        this.streamText += JSON.parse(str).content;
        if (JSON.parse(str)?.stop) {
          stop = true;
        }
      });

      if (stop) {
        this.isFetching = !this.isFetching;
        break;
      }
    }
  }
}
