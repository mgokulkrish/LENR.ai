import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { map } from 'rxjs';
import { APP_CONSTANTS } from '../constants/app.constants';
import { DBService } from '../services/db.service';
import { UtilsService } from '../services/utils.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  public title: string = 'LENR.ai';
  public streamText: string = '';
  public promptText: string = '';

  public stepText = ""

  public isPristine: boolean = false;
  public isFetchingDocs: boolean = false;
  public isLoading: boolean = false;
  public hasError: boolean = false;
  public errorMessage: string = "";

  constructor(private db: DBService, private utils: UtilsService) {
    this.isPristine = true;
  }

  get isInTranstion(): boolean {
    return this.isFetchingDocs || this.isLoading;
  }

  get hasResult(): boolean {
    return !this.isInTranstion && !this.isPristine && !this.hasError;
  }

  getAnswer(): void {
    this.isPristine = false;
    this.hasError = false;
    this.isFetchingDocs = true;

    this.db.getDocs(this.promptText).pipe(
      map((data) => {
        this.isFetchingDocs = false;
        return data.prompt;
      })).subscribe({
        next: (prepared_prompt: string) => {
          // this.getStream(prepared_prompt);
          this.streamText = this.utils.processStreamData(prepared_prompt);

        }, error: (err) => {
          console.error("Error from DB call", err);
          this.isFetchingDocs = false;
          this.hasError = true;
          this.errorMessage = "Error in fetching LENR domain documents";
        }
      });
  }

  private async getStream(prepared_prompt: string) {
    this.isLoading = true;

    let response = await fetch(APP_CONSTANTS.cppServer + "/completion", {
      method: 'POST',
      body: JSON.stringify({
        prompt: prepared_prompt,
        n_predict: 1024,
        stream: true,
      })
    });

    if (response.status !== 200) {
      this.isLoading = false;
      this.hasError = true;
      this.errorMessage = "Error is fetching the LLM data";
      return;
    }

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
        this.isLoading = false;
        break;
      }
    }
  }
}
