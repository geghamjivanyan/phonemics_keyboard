export type KeyAction = "delete" | "clef";

export interface KeyboardKey {
    id: number;
    english: string;
    arabic: string;
    color: string;
    action?: KeyAction;
}
