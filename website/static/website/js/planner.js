document.addEventListener("DOMContentLoaded", function () {

    const destination =
        document.getElementById("destination");

    const duration =
        document.getElementById("duration");

    const travelDate =
        document.getElementById("travel_date");

    const endDate =
        document.getElementById("end_date");

    const pickup =
        document.getElementById("pickup");

    const adults =
        document.getElementById("adults");

    const children =
        document.getElementById("children");


    const summaryDestination =
        document.getElementById("summaryDestination");

    const summaryDuration =
        document.getElementById("summaryDuration");

    const summaryPickup =
        document.getElementById("summaryPickup");

    const summaryDate =
        document.getElementById("summaryDate");

    const summaryTravellers =
        document.getElementById("summaryTravellers");


    /* ==========================================
       MINIMUM DATE = TODAY
    ========================================== */

    if (travelDate) {

        const today = new Date();

        const year =
            today.getFullYear();

        const month =
            String(today.getMonth() + 1)
            .padStart(2, "0");

        const day =
            String(today.getDate())
            .padStart(2, "0");

        travelDate.min =
            `${year}-${month}-${day}`;
    }


    /* ==========================================
       DESTINATION
    ========================================== */

    if (destination) {

        destination.addEventListener(
            "change",
            function () {

                const selectedOption =
                    this.options[this.selectedIndex];

                summaryDestination.textContent =
                    selectedOption.textContent.trim()
                    || "Not selected";

            }
        );

    }


    /* ==========================================
       FORMAT DATE
    ========================================== */

    function formatDate(dateString) {

        if (!dateString) {
            return "Not selected";
        }

        const date =
            new Date(
                dateString + "T00:00:00"
            );

        return date.toLocaleDateString(
            "en-GB",
            {
                day: "2-digit",
                month: "short",
                year: "numeric"
            }
        );
    }


    /* ==========================================
       CALCULATE END DATE
    ========================================== */

    function calculateEndDate() {

        const selectedDuration =
            parseInt(duration.value);

        const startDateValue =
            travelDate.value;


        /*
         * If duration or start date
         * has not been selected,
         * clear the end date.
         */

        if (
            !selectedDuration ||
            !startDateValue
        ) {

            if (endDate) {
                endDate.value = "";
            }

            if (summaryDate) {
                summaryDate.textContent =
                    startDateValue
                        ? formatDate(startDateValue)
                        : "Not selected";
            }

            return;
        }


        /*
         * Create start date.
         *
         * Example:
         *
         * Start: 15 Oct
         * Duration: 5 Days
         *
         * End: 19 Oct
         */

        const calculatedEndDate =
            new Date(
                startDateValue + "T00:00:00"
            );


        calculatedEndDate.setDate(
            calculatedEndDate.getDate()
            + selectedDuration
            - 1
        );


        /*
         * Convert calculated date
         * to YYYY-MM-DD
         */

        const year =
            calculatedEndDate.getFullYear();

        const month =
            String(
                calculatedEndDate.getMonth() + 1
            ).padStart(2, "0");

        const day =
            String(
                calculatedEndDate.getDate()
            ).padStart(2, "0");


        const calculatedEndDateValue =
            `${year}-${month}-${day}`;


        /*
         * Put calculated date
         * into End Date input
         */

        if (endDate) {

            endDate.value =
                calculatedEndDateValue;

        }


        /*
         * Update duration summary
         */

        if (summaryDuration) {

            summaryDuration.textContent =
                selectedDuration +
                (
                    selectedDuration === 1
                        ? " Day"
                        : " Days"
                );

        }


        /*
         * Update date summary
         *
         * Example:
         * 15 Oct 2026 → 19 Oct 2026
         */

        if (summaryDate) {

            summaryDate.textContent =
                formatDate(startDateValue)
                + " → "
                + formatDate(
                    calculatedEndDateValue
                );

        }

    }


    /* ==========================================
       DURATION CHANGE
    ========================================== */

    if (duration) {

        duration.addEventListener(
            "change",
            function () {

                calculateEndDate();

            }
        );

    }


    /* ==========================================
       START DATE CHANGE
    ========================================== */

    if (travelDate) {

        travelDate.addEventListener(
            "change",
            function () {

                calculateEndDate();

            }
        );

    }


    /* ==========================================
       PICKUP
    ========================================== */

    if (pickup) {

        pickup.addEventListener(
            "input",
            function () {

                if (summaryPickup) {

                    summaryPickup.textContent =
                        this.value.trim()
                        || "Not selected";

                }

            }
        );

    }


    /* ==========================================
       TRAVELLERS
    ========================================== */

    function updateTravellers() {

        const adultCount =
            adults.value || 0;

        const childCount =
            children.value || 0;


        let text =
            adultCount +
            (
                adultCount == 1
                    ? " Adult"
                    : " Adults"
            );


        if (childCount > 0) {

            text +=
                " + " +
                childCount +
                (
                    childCount == 1
                        ? " Child"
                        : " Children"
                );

        }


        if (summaryTravellers) {

            summaryTravellers.textContent =
                text;

        }

    }


    /* ==========================================
       ADULT CHANGE
    ========================================== */

    if (adults) {

        adults.addEventListener(
            "change",
            updateTravellers
        );

    }


    /* ==========================================
       CHILDREN CHANGE
    ========================================== */

    if (children) {

        children.addEventListener(
            "change",
            updateTravellers
        );

    }


    /* ==========================================
       INITIAL TRAVELLER SUMMARY
    ========================================== */

    updateTravellers();


    /* ==========================================
       INITIAL END DATE CALCULATION
    ========================================== */

    calculateEndDate();

});