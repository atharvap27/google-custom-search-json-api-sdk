export class GoogleCustomSearchError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "GoogleCustomSearchError";
    }
}
