// ==================================================================
// Class to handle data fetching and transformation for measurements
// ==================================================================

class MeasurementDataHandler {

  // ==============================================
  // Constructor
  // ==============================================
  constructor(endpoint, callback,sens_id,sens_name) {
    // ========================================
    // Config params
    // ========================================
    this.endpoint         = endpoint;
    this.fetch_interval   = 10000;

    // ========================================
    // Class vars
    // ========================================
    this.all_data         = [];
    this.device_datasets  = [];

    this.last_received_id = null;
    this.sensor_id        = sens_id;
    this.sensor_name      = String(sens_name);

    // Function to call when there is updated
    // data available
    this.callback_fn      = callback;

    // ========================================
    // Start the fetch loop
    // ========================================
    this.fetch_loop = setInterval(this.fetchMeasurements.bind(this), this.fetch_interval);
    this.fetchMeasurements(); // Run at creation
  }


  // ==============================================
  // Fetch data from the API
  // ==============================================
  fetchMeasurements() {
    // Create a reference to this obj to reference in AJAX success fn.
    var self = this;

    $.ajax({
      url:      this.endpoint, 
      method:   'GET',
      dataType: 'json',
      data: {
        sensor       : this.sensor_id,
        last_received: this.last_received_id
      },


      success: function(d) {

        // Skip updates if there is no new data
        if (d.length > 0) {
          self.parseDeviceData(d);

          // Update the last received ID
          // Request data is ordered by received time
          self.last_received_id = d[d.length - 1].id;

          // Trigger the callback function with the new
          // raw data.
          self.callback_fn(d);
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
    var filtered_data = [];
    var devices       = [...new Set(d.map(item => item.device))];
    
    // Separate the data by device ID for each dataset
    for (var i = 0; i < devices.length; i++) {
      filtered_data = d.filter(item => item.device == devices[i]);
      this.all_data.push(...filtered_data);

      // Search the array for the object w/ the current device ID
      // dataset_index will be equal to the index of the object if it exists.
      // Undefined if not.
      var dataset_index = this.device_datasets.findIndex(obj => { 
          return obj.device_id === devices[i].id;
      });


      // Append the new data if the object already exists, otherwise create
      // the object.
      if (dataset_index != -1) this.appendMeasurementData(dataset_index, filtered_data);
      else                     this.createDatasetObj(devices[i],         filtered_data);
    }
  }


  // ==============================================
  // Creates a dataset out of the passed 
  // measurement data
  // ==============================================
  createDatasetObj(device, data) {
    // Create a new object for the device data
    this.device_datasets.push(
      {
        device_id: device.id,
        label:     device.name + " " + this.sensor_name+ " Sensor",
        data:      []
      }
    );

    this.appendMeasurementData(this.device_datasets.length - 1, data);
  }



  // ==============================================
  // Appends data to the given obj
  // ==============================================
  appendMeasurementData(index, data) {
      
    // Iterate over each entry and parse data for chart format
    // TODO: This needs to be updated to add data in order of time. 
    //       Otherwise, the chart will go back over itself.
    for (var j = 0; j < data.length; j++) {
      this.device_datasets[index].data.push(
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
    this.sensor_id = id;

    // Reset data and last received id
    this.device_datasets  = [];
    this.all_data         = [];
    this.last_received_id = null;

    this.fetchMeasurements();
  }

}