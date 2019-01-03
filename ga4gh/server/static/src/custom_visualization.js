"use strict";

$(window).on('load', function() {

    makeRequest("datasets/search", {}).then(function(response) {

        const data = JSON.parse(response);
        const listOfDatasetId = data['results']['datasets'];

        let dropdown = document.getElementById("dropdown-menu");

        for (let i = 0; i < listOfDatasetId.length; i++) {
            if (!finalDatasetId.includes(listOfDatasetId[i]['id'])) {
                finalDatasetId.push(listOfDatasetId[i]['id']);
                finalDatasetName.push(listOfDatasetId[i]['name']);
            }
        }

        for (let j = 0; j < finalDatasetId.length; j++) {
            dropdown.innerHTML += '<a class="dropdown-item" id="refresh" href="javascript:void(0)" onclick="refreshDataset(' + j + ')">' + finalDatasetName[j] + '</a>'
        }

        // If the cookie is not set; or if it is set, but not in a list of available datasets
        if (getCookie("datasetId") == null || finalDatasetId.indexOf(getCookie("datasetId")) == -1) {
            datasetId = finalDatasetId[0];
            setCookie("datasetId", datasetId);
            $('#dropdownMenuLink').html('<i class="fas fa-database"></i> ' + finalDatasetName[0]);
            currentDatasetName = splitString(finalDatasetName[0]);
        } else {
            datasetId = getCookie("datasetId");
            $('#dropdownMenuLink').html('<i class="fas fa-database"></i> ' + finalDatasetName[finalDatasetId.indexOf(datasetId)]);
            currentDatasetName = splitString(finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))]);
        }
        initialize();

    }, function(Error) {
        alertBuilder("No data currently available. Please contact a system administrator for assistance.")
    })
});

function refreshDataset(datasetIndex) {
    datasetId = finalDatasetId[datasetIndex];
    document.getElementById("warningMsg").style.display = "none";
    setCookie("datasetId", datasetId);
    $('#dropdownMenuLink').html('<i class="fas fa-database"></i> ' + finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))]);
    currentDatasetName = splitString(finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))]);
    reloadGraphs();
}


var selectPopulated = 0;

let currentDatasetName;

const categories = {
    "patients": ["patientId", "otherIds", "dateOfBirth", "gender", "ethnicity", "race", "provinceOfResidence", "dateOfDeath",
        "causeOfDeath", "autopsyTissueForResearch", "priorMalignancy", "dateOfPriorMalignancy", "familyHistoryAndRiskFactors",
        "familyHistoryOfPredispositionSyndrome", "detailsOfPredispositionSyndrome", "geneticCancerSyndrome",
        "otherGeneticConditionOrSignificantComorbidity", "occupationalOrEnvironmentalExposure"
    ],
    "enrollments": ["patientId", "enrollmentInstitution", "enrollmentApprovalDate", "crossEnrollment", "otherPersonalizedMedicineStudyName",
        "otherPersonalizedMedicineStudyId", "ageAtEnrollment", "eligibilityCategory", "statusAtEnrollment", "primaryOncologistName",
        "primaryOncologistContact", "referringPhysicianName", "referringPhysicianContact", "summaryOfIdRequest", "treatingCentreName", "treatingCentreProvince"
    ],
    "treatments": ["patientId", "courseNumber", "therapeuticModality", "systematicTherapyAgentName", "treatmentPlanType", "treatmentIntent",
        "startDate", "stopDate", "reasonForEndingTheTreatment", "protocolNumberOrCode", "surgeryDetails", "radiotherapyDetails", "chemotherapyDetails",
        "hematopoieticCellTransplant", "immunotherapyDetails", "responseToTreatment", "responseCriteriaUsed", "dateOfRecurrenceOrProgressionAfterThisTreatment",
        "unexpectedOrUnusualToxicityDuringTreatment", "drugListOrAgent", "drugIdNumbers"
    ],
    "samples": ["patientId", "sampleId", "diagnosisId", "localBiobankId", "collectionDate", "collectionHospital", "sampleType", "tissueDiseaseState",
        "anatomicSiteTheSampleObtainedFrom", "cancerType", "cancerSubtype", "pathologyReportId", "morphologicalCode", "topologicalCode",
        "shippingDate", "receivedDate", "qualityControlPerformed", "estimatedTumorContent", "quantity", "units", "associatedBiobank",
        "otherBiobank", "sopFollowed", "ifNotExplainAnyDeviation"
    ],
    "diagnoses": ["patientId", "diagnosisId", "diagnosisDate", "ageAtDiagnosis", "cancerType", "classification", "cancerSite", "histology",
        "methodOfDefinitiveDiagnosis", "sampleType", "sampleSite", "tumorGrade", "gradingSystemUsed", "sitesOfMetastases", "stagingSystem",
        "versionOrEditionOfTheStagingSystem", "specificTumorStageAtDiagnosis", "prognosticBiomarkers", "biomarkerQuantification",
        "additionalMolecularTesting", "additionalTestType", "laboratoryName", "laboratoryAddress", "siteOfMetastases",
        "stagingSystemVersion", "specificStage", "cancerSpecificBiomarkers", "additionalMolecularDiagnosticTestingPerformed", "additionalTest"
    ],
    "tumourboards": ["patientId", "dateOfMolecularTumorBoard", "typeOfSampleAnalyzed", "typeOfTumourSampleAnalyzed", "analysesDiscussed",
        "somaticSampleType", "normalExpressionComparator", "diseaseExpressionComparator",
        "hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancer", "actionableTargetFound",
        "molecularTumorBoardRecommendation", "germlineDnaSampleId", "tumorDnaSampleId", "tumorRnaSampleId",
        "germlineSnvDiscussed", "somaticSnvDiscussed", "cnvsDiscussed", "structuralVariantDiscussed",
        "classificationOfVariants", "clinicalValidationProgress", "typeOfValidation", "agentOrDrugClass",
        "levelOfEvidenceForExpressionTargetAgentMatch", "didTreatmentPlanChangeBasedOnProfilingResult",
        "howTreatmentHasAlteredBasedOnProfiling", "reasonTreatmentPlanDidNotChangeBasedOnProfiling",
        "detailsOfTreatmentPlanImpact", "patientOrFamilyInformedOfGermlineVariant",
        "patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfiling", "summaryReport"
    ],
    "outcomes": ["patientId", "physicalExamId", "dateOfAssessment", "diseaseResponseOrStatus", "otherResponseClassification",
        "minimalResidualDiseaseAssessment", "methodOfResponseEvaluation", "responseCriteriaUsed", "summaryStage",
        "sitesOfAnyProgressionOrRecurrence", "vitalStatus", "height", "weight", "heightUnits", "weightUnits", "performanceStatus"
    ],
    "complications": ["patientId", "date", "lateComplicationOfTherapyDeveloped", "lateToxicityDetail", "suspectedTreatmentInducedNeoplasmDeveloped", "treatmentInducedNeoplasmDetails"],
    "consents": ["patientId", "consentId", "consentDate", "consentVersion", "patientConsentedTo", "reasonForRejection",
        "wasAssentObtained", "dateOfAssent", "assentFormVersion", "ifAssentNotObtainedWhyNot", "reconsentDate", "reconsentVersion",
        "consentingCoordinatorName", "previouslyConsented", "nameOfOtherBiobank", "hasConsentBeenWithdrawn",
        "dateOfConsentWithdrawal", "typeOfConsentWithdrawal", "reasonForConsentWithdrawal", "consentFormComplete"
    ]
}
alertCloser();

let endpoints = ["patients", "enrollments", "treatments", "samples", "diagnoses", "tumourboards", "outcomes", "complications", "consents"];
let types = ["bar", "column", "pie", "scatter"]
let type1 = types[Math.floor(Math.random() * types.length)];
let type2 = types[Math.floor(Math.random() * types.length)];

$("#table1").off("change").change(function() {
    document.getElementById("key1").innerHTML = "";
    selectPopulator("key1", categories[$("#table1").val()]);
});

$("#table2").off("change").change(function() {
    document.getElementById("key2").innerHTML = "";
    selectPopulator("key2", categories[$("#table2").val()]);
});

$("#adv1_confirm").off('click').click(function() {
    document.getElementById("adv1").innerHTML = '<div class="loader_bar"></div>';
    countRequest($("#table1").val(), [$("#key1").val()], datasetId).then(function(response) {
        if (response[$("#key1").val()] == undefined) {
            document.getElementById("adv1").innerHTML = "<p class='noPermission'>You don't have access to this data.</p>";
        } else {
            var selectedKey = $("#key1").val();
            singleLayerDrawer("adv1", $("#type1").val(), "Distribution of " + splitString(selectedKey), currentDatasetName + " " + splitString($("#table1").val()), response[$("#key1").val()])
        }
    })
});

$("#adv2_confirm").off('click').click(function() {
    document.getElementById("adv2").innerHTML = '<div class="loader_bar"></div>';
    countRequest($("#table2").val(), [$("#key1").val()], datasetId).then(function(response) {
        if (response[$("#key2").val()] == undefined) {
            document.getElementById("adv2").innerHTML = "<p class='noPermission'>You don't have access to this data.</p>";
        } else {
            var selectedKey = $("#key2").val();
            singleLayerDrawer("adv2", $("#type2").val(), "Distribution of " + splitString(selectedKey), currentDatasetName + " " + splitString($("#table2").val()), response[$("#key2").val()])
        }
    })
});

function initialize() {
    if (selectPopulated == 0) {
        selectPopulator("table1", endpoints);
        selectPopulator("table2", endpoints);
        selectPopulator("key1", categories["patients"]);
        selectPopulator("key2", categories["patients"]);
        selectPopulator("type1", types);
        selectPopulator("type2", types);
        selectPopulated = 1;

        document.getElementById("key1").selectedIndex = "6";
        document.getElementById("key2").selectedIndex = "6";
        document.getElementById("type1").selectedIndex = JSON.stringify(types.indexOf(type1));
        document.getElementById("type2").selectedIndex = JSON.stringify(types.indexOf(type2));

        countRequest($("#table1").val(), [$("#key1").val()], datasetId).then(function(response) {
            if (response[$("#key1").val()] == undefined) {
                document.getElementById("adv1").innerHTML = "<p class='noPermission'>You don't have access to this data.</p>";
                document.getElementById("adv2").innerHTML = "<p class='noPermission'>You don't have access to this data.</p>";
            } else {
                singleLayerDrawer("adv1", type1, "Distribution of Province Of Residence", currentDatasetName + " " + "Patients", response[$("#key1").val()])
                singleLayerDrawer("adv2", type2, "Distribution of Province Of Residence", currentDatasetName + " " + "Patients", response[$("#key2").val()])
            }
        })
    }
}

function reloadGraphs() {
    document.getElementById('adv1_confirm').click();
    document.getElementById('adv2_confirm').click();
}

function selectPopulator(id, array) {
    let selectId = document.getElementById(id);

    for (let i = 0; i < array.length; i++) {
        selectId.options[selectId.options.length] = new Option(splitString(array[i]), array[i])
    }
}

// Capitalize the first letter of a string
function splitString(newString) {
    let splitted = newString.replace(/([a-z])([A-Z])/g, '$1 $2')
    let capitalized = splitted.charAt(0).toUpperCase() + splitted.substr(1);
    return capitalized;
}

function highChartSeriesObjectMaker(nameArray, dataArray) {
    var tempObj = {};
    var seriesObjList = [];
    var tempDataArray = [];
    for (var i = 0; i < nameArray.length; i++) {
        tempObj = {};
        tempObj['name'] = nameArray[i];
        tempObj['y'] = dataArray[i];
        seriesObjList.push(tempObj);
    }
    return seriesObjList;
}

function singleLayerDrawer(id, type, title, subtitle, count) {
    var categories = Object.keys(count);
    var values = Object.values(count);
    var seriesArray = highChartSeriesObjectMaker(categories, values);

    Highcharts.chart(id, {
        chart: {
            type: type,
            zoomType: 'xy'
        },
        credits: {
            enabled: false
        },
        title: {
            text: title
        },
        subtitle: {
            text: subtitle
        },
        xAxis: {
            type: 'category'
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true
                }
            }
        },
        series: [{
            name: 'count',
            colorByPoint: true,
            data: seriesArray
        }]
    });
}