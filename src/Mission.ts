import { readFileSync } from 'fs';
import { parse } from 'csv-parse/sync';

export class Mission {
    private depthProfile: number[];
    private targetReference: number[];

    constructor(depthProfile: number[], targetReference: number[]) {
        this.depthProfile = depthProfile;
        this.targetReference = targetReference;
    }

    public static fromCSV(filepath: string): Mission {
        const fileContent = readFileSync(filepath, 'utf-8');
        const records = parse(fileContent, {
            columns: true,
            skip_empty_lines: true
        });

        const depthProfile = records.map((row: any) => Number(row.depth_profile));
        const targetReference = records.map((row: any) => Number(row.target_reference));

        return new Mission(depthProfile, targetReference);
    }

    public getDepthProfile(): number[] {
        return this.depthProfile;
    }

    public getTargetReference(): number[] {
        return this.targetReference;
    }
}
