document.addEventListener("DOMContentLoaded", function () {
    var agencySelect = document.getElementById("agency-select");
    var agentSelect = document.getElementById("agent-select");
    const insightsElem = document.getElementById("insightsElem");  
    var policiesSoldYtdElem = document.getElementById("policies-sold-ytd-value");

    var claims_processed = document.getElementById("claims-value");
    var frauds_processed = document.getElementById("fraud-value");
    const agentNameElement = document.getElementById('agent-name'); // Element to update
    var state_name  = document.getElementById("state-name");

  
    // Add default options to agency and agent dropdowns
    agencySelect.innerHTML = '<option value="" disabled selected>Select Agency</option>';
    agentSelect.innerHTML = '<option value="" disabled selected>Select Agent</option>';

    fetch("/agency_names")
        .then(response => response.json())
        .then(data => {
            Object.keys(data.agency_data).forEach(agencyName => {
                var option = document.createElement("option");
                option.value = agencyName;
                option.textContent = agencyName;
                agencySelect.appendChild(option);
            });
  
            // Event listener for agency selection
            agencySelect.addEventListener("change", function () {
                var selectedAgency = agencySelect.value;
  
                // Clear the agent select dropdown and set a default option
                agentSelect.innerHTML = '<option value="" disabled selected>Select Agent</option>';
  
                // Populate agent names based on the selected agency
                data.agency_data[selectedAgency].forEach(agentName => {
                    var option = document.createElement("option");
                    option.value = agentName;
                    option.textContent = agentName;
                    agentSelect.appendChild(option);
                });

                const selectedAgentName = agentSelect.value;
            
                // Update the agent name in the content
                agentNameElement.textContent = selectedAgentName;

            });




            // Event listener for agent selection to fetch new data
            agentSelect.addEventListener("change", function () {
                var selectedAgent = agentSelect.value;

                if (selectedAgent === "") {
                    // Reset the displayed metrics data if no agent is selected
                    policiesSoldYtdElem.textContent = "";
                    claims_processed.textContent = "";
                    frauds_processed.textContent = "";
                    insightsElem.innerText = "";
                    state_name.textContent = "";
                } else {
                    // Fetch data from the metrics_data endpoint based on the selected agent
                    fetch(`/metrics_data?agent=${selectedAgent}`)
                        .then(response => response.json())
                        .then(metricsData => {
                            // Update the placeholders with the fetched data
                            policiesSoldYtdElem.textContent = metricsData.policy_issued;
                            claims_processed.textContent = metricsData.claims_processed;
                            frauds_processed.textContent = metricsData.fraud_detected;
                            state_name.textContent = metricsData.state_name;

                          

                            let formattedInsights = metricsData.insights.replace(/#/g, '\n');
                            insightsElem.innerText = formattedInsights;



                            const totalRanks = metricsData.total_ranks;
                            const currentRank =metricsData.rank;
                          
                        
                            const pointer = document.getElementById("pointer");
                            const percentage = (currentRank / totalRanks) * 100;
                        
                            if (percentage >= 50) {
                              pointer.style.backgroundColor = "red";
                            } else {
                              pointer.style.backgroundColor = "green";
                            }
                        
                            pointer.style.left = `calc(${percentage}% - 2.5px)`;
                            rankNumber.textContent = currentRank; 


                            const apiResponse = JSON.parse(metricsData.forecast)

                            console.log(apiResponse)

                            const months = Object.keys(apiResponse.policy_sold);
    const policySoldData = Object.values(apiResponse.policy_sold);
    const claimsData = Object.values(apiResponse.claims);
    const fraudData = Object.values(apiResponse.fraud);

    const data = {
      labels: months,
      datasets: [
        {
          label: "Policy Sold",
          data: policySoldData,
          borderColor: "blue",
          fill: false
        },
        {
          label: "Claims",
          data: claimsData,
          borderColor: "green",
          fill: false
        },
        {
          label: "Fraud",
          data: fraudData,
          borderColor: "red",
          fill: false
        }
      ]
    };

    const config = {
        type: "line",
        data: data,
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: "Forecast"
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 20   ,
              ticks: {
                stepSize: 5, // Set the step size to 5 to show multiples of 5
              },
            },
          },
        },
      };
      
      const ctx = document.getElementById("metricsChart").getContext("2d");
      new Chart(ctx, config);
      

      chart.data = data;
            chart.update();





                        })
                        .catch(error => console.error("Error fetching metrics data:", error));
                }
            });
        })
        .catch(error => console.error("Error fetching agency and agent data:", error));
});
