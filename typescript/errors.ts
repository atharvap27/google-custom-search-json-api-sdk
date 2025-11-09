export class GoogleCustomSearchAPIError extends Error {
  constructor(message: string) {
    super(message);
    Object.setPrototypeOf(this, GoogleCustomSearchAPIError.prototype);
    this.name = 'GoogleCustomSearchAPIError';
  }
}

export class GoogleCustomSearchAuthError extends Error {
  constructor(message: string) {
    super(message);
    Object.setPrototypeOf(this, GoogleCustomSearchAuthError.prototype);
    this.name = 'GoogleCustomSearchAuthError';
  }
}
