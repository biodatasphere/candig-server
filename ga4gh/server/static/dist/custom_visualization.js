"use strict";$(window).on("load",function(){makeRequest("datasets/search",{}).then(function(a){const b=JSON.parse(a),c=b.results.datasets;let d=document.getElementById("dropdown-menu");for(let b=0;b<c.length;b++)finalDatasetId.includes(c[b].id)||(finalDatasetId.push(c[b].id),finalDatasetName.push(c[b].name));for(let b=0;b<finalDatasetId.length;b++)d.innerHTML+="<a class=\"dropdown-item\" id=\"refresh\" href=\"javascript:void(0)\" onclick=\"refreshDataset("+b+")\">"+finalDatasetName[b]+"</a>";null==getCookie("datasetId")||-1==finalDatasetId.indexOf(getCookie("datasetId"))?(datasetId=finalDatasetId[0],setCookie("datasetId",datasetId),$("#dropdownMenuLink").html("<i class=\"fas fa-database\"></i> "+finalDatasetName[0]),currentDatasetName=splitString(finalDatasetName[0])):(datasetId=getCookie("datasetId"),$("#dropdownMenuLink").html("<i class=\"fas fa-database\"></i> "+finalDatasetName[finalDatasetId.indexOf(datasetId)]),currentDatasetName=splitString(finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))])),initialize()},function(){alertBuilder("No data currently available. Please contact a system administrator for assistance.")})});function refreshDataset(a){datasetId=finalDatasetId[a],document.getElementById("warningMsg").style.display="none",setCookie("datasetId",datasetId),$("#dropdownMenuLink").html("<i class=\"fas fa-database\"></i> "+finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))]),currentDatasetName=splitString(finalDatasetName[finalDatasetId.indexOf(getCookie("datasetId"))]),reloadGraphs()}var selectPopulated=0;let currentDatasetName;const categories={patients:["patientId","otherIds","dateOfBirth","gender","ethnicity","race","provinceOfResidence","dateOfDeath","causeOfDeath","autopsyTissueForResearch","priorMalignancy","dateOfPriorMalignancy","familyHistoryAndRiskFactors","familyHistoryOfPredispositionSyndrome","detailsOfPredispositionSyndrome","geneticCancerSyndrome","otherGeneticConditionOrSignificantComorbidity","occupationalOrEnvironmentalExposure"],enrollments:["patientId","enrollmentInstitution","enrollmentApprovalDate","crossEnrollment","otherPersonalizedMedicineStudyName","otherPersonalizedMedicineStudyId","ageAtEnrollment","eligibilityCategory","statusAtEnrollment","primaryOncologistName","primaryOncologistContact","referringPhysicianName","referringPhysicianContact","summaryOfIdRequest","treatingCentreName","treatingCentreProvince"],treatments:["patientId","courseNumber","therapeuticModality","systematicTherapyAgentName","treatmentPlanType","treatmentIntent","startDate","stopDate","reasonForEndingTheTreatment","protocolNumberOrCode","surgeryDetails","radiotherapyDetails","chemotherapyDetails","hematopoieticCellTransplant","immunotherapyDetails","responseToTreatment","responseCriteriaUsed","dateOfRecurrenceOrProgressionAfterThisTreatment","unexpectedOrUnusualToxicityDuringTreatment","drugListOrAgent","drugIdNumbers"],samples:["patientId","sampleId","diagnosisId","localBiobankId","collectionDate","collectionHospital","sampleType","tissueDiseaseState","anatomicSiteTheSampleObtainedFrom","cancerType","cancerSubtype","pathologyReportId","morphologicalCode","topologicalCode","shippingDate","receivedDate","qualityControlPerformed","estimatedTumorContent","quantity","units","associatedBiobank","otherBiobank","sopFollowed","ifNotExplainAnyDeviation"],diagnoses:["patientId","diagnosisId","diagnosisDate","ageAtDiagnosis","cancerType","classification","cancerSite","histology","methodOfDefinitiveDiagnosis","sampleType","sampleSite","tumorGrade","gradingSystemUsed","sitesOfMetastases","stagingSystem","versionOrEditionOfTheStagingSystem","specificTumorStageAtDiagnosis","prognosticBiomarkers","biomarkerQuantification","additionalMolecularTesting","additionalTestType","laboratoryName","laboratoryAddress","siteOfMetastases","stagingSystemVersion","specificStage","cancerSpecificBiomarkers","additionalMolecularDiagnosticTestingPerformed","additionalTest"],tumourboards:["patientId","dateOfMolecularTumorBoard","typeOfSampleAnalyzed","typeOfTumourSampleAnalyzed","analysesDiscussed","somaticSampleType","normalExpressionComparator","diseaseExpressionComparator","hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancer","actionableTargetFound","molecularTumorBoardRecommendation","germlineDnaSampleId","tumorDnaSampleId","tumorRnaSampleId","germlineSnvDiscussed","somaticSnvDiscussed","cnvsDiscussed","structuralVariantDiscussed","classificationOfVariants","clinicalValidationProgress","typeOfValidation","agentOrDrugClass","levelOfEvidenceForExpressionTargetAgentMatch","didTreatmentPlanChangeBasedOnProfilingResult","howTreatmentHasAlteredBasedOnProfiling","reasonTreatmentPlanDidNotChangeBasedOnProfiling","detailsOfTreatmentPlanImpact","patientOrFamilyInformedOfGermlineVariant","patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfiling","summaryReport"],outcomes:["patientId","physicalExamId","dateOfAssessment","diseaseResponseOrStatus","otherResponseClassification","minimalResidualDiseaseAssessment","methodOfResponseEvaluation","responseCriteriaUsed","summaryStage","sitesOfAnyProgressionOrRecurrence","vitalStatus","height","weight","heightUnits","weightUnits","performanceStatus"],complications:["patientId","date","lateComplicationOfTherapyDeveloped","lateToxicityDetail","suspectedTreatmentInducedNeoplasmDeveloped","treatmentInducedNeoplasmDetails"],consents:["patientId","consentId","consentDate","consentVersion","patientConsentedTo","reasonForRejection","wasAssentObtained","dateOfAssent","assentFormVersion","ifAssentNotObtainedWhyNot","reconsentDate","reconsentVersion","consentingCoordinatorName","previouslyConsented","nameOfOtherBiobank","hasConsentBeenWithdrawn","dateOfConsentWithdrawal","typeOfConsentWithdrawal","reasonForConsentWithdrawal","consentFormComplete"]};alertCloser();let endpoints=["patients","enrollments","treatments","samples","diagnoses","tumourboards","outcomes","complications","consents"],types=["bar","column","pie","scatter"],type1=types[Math.floor(Math.random()*types.length)],type2=types[Math.floor(Math.random()*types.length)];$("#table1").off("change").change(function(){document.getElementById("key1").innerHTML="",selectPopulator("key1",categories[$("#table1").val()])}),$("#table2").off("change").change(function(){document.getElementById("key2").innerHTML="",selectPopulator("key2",categories[$("#table2").val()])}),$("#adv1_confirm").off("click").click(function(){document.getElementById("adv1").innerHTML="<div class=\"loader_bar\"></div>",makeRequest($("#table1").val()+"/search",{datasetId:datasetId}).then(function(a){var b=JSON.parse(a).results[$("#table1").val()],c=$("#key1").val();if(b[0][c]==null)document.getElementById("adv1").innerHTML="<p class='noPermission'>You don't have access to this data.</p>";else{var d=groupBy(b,c);singleLayerDrawer("adv1",$("#type1").val(),"Distribution of "+splitString(c),currentDatasetName+" "+splitString($("#table1").val()),d)}})}),$("#adv2_confirm").off("click").click(function(){document.getElementById("adv2").innerHTML="<div class=\"loader_bar\"></div>",makeRequest($("#table2").val()+"/search",{datasetId:datasetId}).then(function(a){var b=JSON.parse(a).results[$("#table2").val()],c=$("#key2").val();if(b[0][c]==null)document.getElementById("adv2").innerHTML="<p class='noPermission'>You don't have access to this data.</p>";else{var d=groupBy(b,c);singleLayerDrawer("adv2",$("#type2").val(),"Distribution of "+splitString(c),currentDatasetName+" "+splitString($("#table1").val()),d)}})});function initialize(){0==selectPopulated&&(selectPopulator("table1",endpoints),selectPopulator("table2",endpoints),selectPopulator("key1",categories.patients),selectPopulator("key2",categories.patients),selectPopulator("type1",types),selectPopulator("type2",types),selectPopulated=1,document.getElementById("key1").selectedIndex="6",document.getElementById("key2").selectedIndex="6",document.getElementById("type1").selectedIndex=JSON.stringify(types.indexOf(type1)),document.getElementById("type2").selectedIndex=JSON.stringify(types.indexOf(type2)),makeRequest("patients/search",{datasetId:datasetId}).then(function(a){var b=JSON.parse(a).results.patients,c=groupBy(b,"provinceOfResidence");singleLayerDrawer("adv1",type1,"Distribution of Province Of Residence",currentDatasetName+" Patients",c),singleLayerDrawer("adv2",type2,"Distribution of Province Of Residence",currentDatasetName+" Patients",c)}))}function reloadGraphs(){document.getElementById("adv1_confirm").click(),document.getElementById("adv2_confirm").click()}function selectPopulator(a,b){let c=document.getElementById(a);for(let d=0;d<b.length;d++)c.options[c.options.length]=new Option(splitString(b[d]),b[d])}function splitString(a){let b=a.replace(/([a-z])([A-Z])/g,"$1 $2"),c=b.charAt(0).toUpperCase()+b.substr(1);return c}function highChartSeriesObjectMaker(a,b){for(var c={},d=[],e=0;e<a.length;e++)c={},c.name=a[e],c.y=b[e],d.push(c);return d}function singleLayerDrawer(a,b,c,d,e){var f=Object.keys(e),g=Object.values(e),h=highChartSeriesObjectMaker(f,g);Highcharts.chart(a,{chart:{type:b,zoomType:"xy"},credits:{enabled:!1},title:{text:c},subtitle:{text:d},xAxis:{type:"category"},legend:{enabled:!1},plotOptions:{series:{borderWidth:0,dataLabels:{enabled:!0}}},series:[{name:"count",colorByPoint:!0,data:h}]})}