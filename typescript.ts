const users = [
    { id: 1, name: 'Alice', age: 17, emailVerified: true, lastLoginDays: 10 },
    { id: 2, name: 'Bob', age: 34, emailVerified: false, lastLoginDays: 400 },
    { id: 3, name: 'Carol', age: 72, emailVerified: true, lastLoginDays: 800 },
    { id: 4, name: 'Dave', age: 16, emailVerified: false, lastLoginDays: 5 },
    { id: 5, name: 'Eve', age: 45, emailVerified: true, lastLoginDays: 200 }
];

function analyzeUsers(userList) {
    const report = {
        total: 0,
        minors: 0,
        adults: 0,
        seniors: 0,
        verifiedActive: 0,
        verifiedInactive: 0,
        unverified: 0,
        inactiveUsers: []
    };

    for (let i = 0; i < userList.length; i++) {
        const u = userList[i];
        report.total++;

        if (typeof u.age !== 'number') {
            // skip counting age if invalid
        } else if (u.age < 18) {
            report.minors++;
        } else if (u.age < 65) {
            report.adults++;
        } else {
            report.seniors++;
        }

        if (u.emailVerified) {
            if (u.lastLoginDays <= 365) {
                report.verifiedActive++;
            } else {
                report.verifiedInactive++;
                report.inactiveUsers.push(u.id);
            }
        } else {
            if (u.lastLoginDays <= 30) {
                report.unverified++;
            } else {
                report.unverified++;
                report.inactiveUsers.push(u.id);
            }
        }
    }

    return report;
}
