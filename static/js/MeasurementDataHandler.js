// ==================================================================
// Class to handle data fetching and transformation for measurements
// ==================================================================

class MeasurementDataHandler {

  // ==============================================
  // Constructor
  // ==============================================
  constructor(callback) {
    // Config params
    this.fetch_interval   = 5000;

    this.all_data         = [];
    this.device_datasets  = [];

    this.last_received_id = null;
    this.sensor_id        = null;

    // Function to call when there is updated
    // data available
    this.callback_fn      = callback;
  }


  // ==============================================
  // Constructor
  // TODO: Change addresss to configurable route
  // ==============================================
  fetchMeasurements() {
    $.ajax({
      url:      "http://localhost:8000/api/measurements/", 
      method:   'GET',
      dataType: 'json',
      data: {
        sensor       : this.sensor_id,
        last_received: this.last_received_id
      },


      success: function(d) {

        // Skip updates if there is no new data
        if (d.length > 0) {
          parseDeviceData(d);

          // Update the last received ID
          // Request data is ordered by received time
          this.last_received_id = d[d.length - 1].id;

          updateChart();
          updateTable(d);
        }
      }
    });
  }

  // ==============================================
  // Find each of the unique devices from the data 
  // and separate the measurements into datasets 
  // for each device.
  // ==============================================
  parseDeviceData(d) {
    devices = [...new Set(d.map(item => item.device))];

    // Separate the data by device ID for each dataset
    for (i = 0; i < devices.length; i++) {
      filtered_data = d.filter(item => item.device == devices[i]);
      all_data.push(...filtered_data);

      // Search the array for the object w/ the current device ID
      // dataset_index will be equal to the index of the object if it exists.
      // Undefined if not.
      dataset_index = device_data.findIndex(obj => { 
          return obj.label === devices[i];
      });


      // Append the new data if the object already exists, otherwise create
      // the object.
      if (dataset_index != -1) appendMeasurementData(dataset_index, filtered_data);
      else                     createDatasetObj(devices[i],         filtered_data);
    }
  }


  // ==============================================
  // Creates a dataset out of the passed 
  // measurement data
  // ==============================================
  createDatasetObj(label, data) {
    // Create a new object for the device data
    device_data.push(
      {
        label: label,
        data:  []
      }
    );

    appendMeasurementData(device_data.length - 1, data);
  }



  // ==============================================
  // Appends data to the given obj
  // ==============================================
  appendMeasurementData(index, data) {
      
    // Iterate over each entry and parse data for chart format
    // TODO: This needs to be updated to add data in order of time. 
    //       Otherwise, the chart will go back over itself.
    for (j = 0; j < data.length; j++) {
        device_data[index].data.push(
            {
                x: data[j].datetime, // TODO: Needs to be converted
                y: data[j].value
            }
        );
    }
  }


  // ==============================================
  // Function to set the HTML parsing args
  // ==============================================
  setSensorID(id) {
    sensor_id = id;

    // Reset data and last received id
    device_data      = [];
    table_data       = [];
    last_received_id = null;

    fetchMeasurements();
  }

}