export class GoogleAPIError extends Error {
  public statusCode?: number;
  public details: any;

  constructor(statusCode: number | undefined, details: any) {
    super(`Google API request failed: ${statusCode} - ${details}`);
    this.statusCode = statusCode;
    this.details = details;
    Object.setPrototypeOf(this, GoogleAPIError.prototype);
  }
}
