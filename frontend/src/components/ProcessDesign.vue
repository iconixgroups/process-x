<template>
  <div class="process-design">
    <div class="editor-header">
      <h2>Process Design</h2>
      <button @click="saveProcess" class="save-button">Save Process</button>
    </div>
    <div class="editor-container">
      <div id="processDesignEditor"></div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import * as d3 from 'd3';

export default {
  name: 'ProcessDesign',
  data() {
    return {
      graph: null,
      parent: null
    };
  },
  mounted() {
    this.initializeGraph();
  },
  methods: {
    ...mapActions('design', ['designProcess']),
    initializeGraph() {
      this.graph = new mxGraph(this.$el.querySelector('#processDesignEditor'));
      this.parent = this.graph.getDefaultParent();

      this.graph.getModel().beginUpdate();
      try {
        // Example process design
        const start = this.graph.insertVertex(this.parent, null, 'Start', 20, 20, 80, 30);
        const step1 = this.graph.insertVertex(this.parent, null, 'Step 1', 200, 20, 80, 30);
        const end = this.graph.insertVertex(this.parent, null, 'End', 380, 20, 80, 30);

        this.graph.insertEdge(this.parent, null, '', start, step1);
        this.graph.insertEdge(this.parent, null, '', step1, end);
      } finally {
        this.graph.getModel().endUpdate();
        new mxRubberband(this.graph);
        new mxKeyHandler(this.graph);
      }
    },
    saveProcess() {
      const encoder = new mxCodec();
      const result = encoder.encode(this.graph.getModel());
      const xml = mxUtils.getXml(result);

      this.designProcess({
        moduleId: this.$route.params.moduleId,
        processType: 'BPMN',
        details: xml
      }).then(() => {
        this.$emit('processDesigned');
      }).catch(error => {
        console.error('Failed to save process design:', error);
      });
    }
  }
};
</script>

<style scoped>
.process-design {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.editor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.editor-container {
  flex-grow: 1;
  overflow: hidden;
}

.save-button {
  padding: 5px 15px;
  background-color: #5cb85c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.save-button:hover {
  background-color: #4cae4c;
}
</style>