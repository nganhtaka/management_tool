<template>
  <div class="card shadow" :class="type === 'dark' ? 'bg-default' : ''" >
    <div
      class="card-header border-0"
      :class="type === 'dark' ? 'bg-transparent' : ''"
    >
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0" :class="type === 'dark' ? 'text-white' : ''">
            {{ title }}
          </h3>
        </div>
        <div class="col text-right">
          <base-button type="primary" size="sm" @click="this.add_days_to_show(0)">Reset</base-button>
          <base-button type="primary" size="sm" @click="this.add_days_to_show(-1)">-</base-button>
          <base-button type="primary" size="sm" @click="this.add_days_to_show(1)">+</base-button>
          <base-button type="primary" size="sm" @click="this.newTask">Add task</base-button>
        </div>
      </div>
    </div>

    <div class="table-responsive" style="height:80vh">
      <base-table
        class="table align-items-center table-flush"
        :class="type === 'dark' ? 'table-dark' : ''"
        :thead-classes="type === 'dark' ? 'thead-dark' : 'thead-light'"
        tbody-classes="list"
        :data="tableData"
        :columns="columnsTable"
      >
        <template v-slot:default="row">
          <th scope="row">
            <div class="media align-items-center">
              <div class="media-body">
                <span class="name mb-0 text-sm">{{ row.item.user_name }}</span>
              </div>
            </div>
          </th>
          <td class="task1" v-for="tasks in row.item.tasks" :key="tasks">
            <div v-for="task in tasks" :key="task">
              <div v-for="item in task" :key="item">
                <base-button size="sm" :type="item.task_type"
                  @click="openTask(item.task_name,item.task_action, item.task_type)">
                  {{ item.task_name }} : {{ item.task_action }}
                </base-button>
              </div>
            </div>
          </td>
        </template>
      </base-table>
    </div>

    <div
      class="card-footer d-flex justify-content-end"
      :class="type === 'dark' ? 'bg-transparent' : ''"
    >
    </div>
  </div>
  <div>
  <modal v-model:show="this.showModal"
           :gradient="actualTask.task_type"
           modal-classes="modal-dialog-centered modal-sm">
            <form role="form">
                <base-input formClasses="input-group-alternative mb-3"
                            placeholder="Numero de ticket"
                            :value="actualTask.task_name"
                            addon-left-icon="ni ni-email-83">
                </base-input>
                <base-input formClasses="input-group-alternative mb-3"
                            placeholder="Actions"
                            :value="actualTask.task_action"
                            addon-left-icon="ni ni-lock-circle-open">
                </base-input>
                <div class="text-center">
                    <base-button type="primary" @click="this.changeTask">Save changes</base-button>
                    <base-button type="secondary" @click="this.showModal = false">Close</base-button>
                </div>
            </form>
    </modal>
</div>
</template>
<script>
import moment from 'moment';

export default {
  name: "DailyTable",
  props: {
    type: {
      type: String,
    },
    title: String,
  },
  data() {
    return {
      showModal:false,
      actualTask : {task_name:"", task_action:"", task_type:""},
      nb_day_to_show : 7,
      nb_day_default: 7,
      today : new Date(),
      columnsTable: [],
    }
  },
  methods: {
    async getData() {
      try {
        // const myRequest = new Request('',{method: 'GET'});
        // const response = await fetch(myRequest);
        // this.results = await response.json();
        this.results =  [
          {
            "user_name": "Anh",
            "tasks" : [
              {"task" : [
                {
                    "task_action": "test",
                    "date_action": "Mon, 06 Dec 2021 23:00:00 GMT",
                    "status": 0,
                    "task_name": "ticket 01",
                    "task_type": "l-success"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Mon, 06 Dec 2021 23:00:00 GMT",
                    "status": 1,
                    "task_name": "ticket 02",
                    "user_name": "Anh",
                    "task_type": "success"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Tue, 07 Dec 2021 23:00:00 GMT",
                    "status": 3,
                    "task_name": "ticket 04",
                    "user_name": "Anh",
                    "task_type": "l-info"
                }
              ]},
              {"task" : [
                {
                    "task_action": "analyse",
                    "date_action": "Tue, 07 Dec 2021 23:00:00 GMT",
                    "status": 2,
                    "task_name": "ticket 03",
                    "task_type": "info"
                }
              ]},
              {"tasks" : [
                {
                    "task_action": "analyse",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 05",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 06",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]}, 
              {"tasks" : [
                {
                    "task_action": "analyse",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 05",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 06",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]},
              {"tasks" : [
                {
                    "task_action": "analyse",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 05",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 06",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]},
              {"tasks" : [
                {
                    "task_action": "analyse",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 05",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 06",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]}, 
              {"tasks" : [
                {
                    "task_action": "analyse",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 05",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 06",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]}
            ]
          },
          {
            "user_name": "Audrey",
            "tasks" : [
              {"task" : [
                {
                    "task_action": "test 2",
                    "date_action": "Mon, 06 Dec 2021 23:00:00 GMT",
                    "status": 0,
                    "task_name": "ticket 07",
                    "task_type": "l-info",
                },
                {
                    "task_action": "en cours",
                    "date_action": "Mon, 06 Dec 2021 23:00:00 GMT",
                    "status": 1,
                    "task_name": "ticket 08",
                    "user_name": "Audrey",
                    "task_type": "success"
                },
                {
                    "task_action": "en cours 2",
                    "date_action": "Tue, 07 Dec 2021 23:00:00 GMT",
                    "status": 3,
                    "task_name": "ticket 09",
                    "user_name": "Audrey",
                    "task_type": "l-info"
                }
              ]},
              {"task" : [
                {
                    "task_action": "analyse 3 ",
                    "date_action": "Tue, 07 Dec 2021 23:00:00 GMT",
                    "status": 2,
                    "task_name": "ticket 10",
                    "task_type": "info"
                }
              ]},
              {"tasks" : [
                {
                    "task_action": "analyse05",
                    "date_action": "Wed, 08 Dec 2021  23:00:00 GMT",
                    "status": 4,
                    "task_name": "ticket 11",
                    "task_type": "warning"
                },
                {
                    "task_action": "en cours05",
                    "date_action": "Wed, 08 Dec 2021 23:00:00 GMT",
                    "status": 5,
                    "task_name": "ticket 12",
                    "user_name": "Anh",
                    "task_type": "progress"
                }
              ]}, 
              {"task" : []}, {"task" : []}, {"task" : []}, {"task" : []}
            ]
          }
        ];
        this.tableData = this.results;
        /*for (var i = 0; i < 7; i++) {
          this.weekActual
        } */
       
      } catch (error) {
        console.log(error);
      }
    },
    get_days_to_show() {
      let d = new Date(this.today);
      this.weekActual = [];
      var week= new Array(); 
      // Starting Monday not Sunday
      var list_day_of_week = ['Dimanche','Lundi ', 'Mardi ', 'Mercredi ', 'Jeudi ', 'Vendredi ', 'Samedi '];
      d.setDate((d.getDate() - Math.floor(this.nb_day_to_show / 2)));
      while (d.getDay() > 5)
        d.setDate(d.getDate() - 1);
      
      week.push('Teams');
      for (var i = 0; i < this.nb_day_to_show; i++) {
          week.push(
              list_day_of_week[d.getDay()] + moment(new Date(d)).format('DD/MM')
          );
          this.weekActual.push(new Date(d));
          if (d.getDay() == 5) { 
            // if friday, go next monday
            d.setDate(d.getDate() + 3);
          } else {
            d.setDate(d.getDate() +1);
          }
      }
      return week; 
    },
    _init() {
    this.columnsTable = this.get_days_to_show();
    this.getData();
    },
    add_days_to_show(more) {
      if (more > 0)
        this.nb_day_to_show+=2;
      else if (this.nb_day_to_show >= this.nb_day_default && more < 0)
        this.nb_day_to_show-=2;
      else 
        this.nb_day_to_show=this.nb_day_default;
      this._init();
    },
    openTask(task_name, task_action, task_type) {
      this.showModal = true;
      this.actualTask = {
        task_name : task_name,
        task_action : task_action, 
        task_type : task_type
      }      
    },
    changeTask() {
      // save data
      this.resetTask();
      this.showModal = false;
    },
    newTask(){ // new modal with dropdown tickets
      this.resetTask();
      this.showModal = true;
    },
    resetTask(){
      this.actualTask = {task_name:"", task_action:"", task_type:""};
    }
  }, 
  created() {
    this._init();
  }
};
</script>
<style></style>
