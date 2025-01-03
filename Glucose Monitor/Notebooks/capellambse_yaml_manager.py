import yaml
from jinja2 import Template
import capellambse

class CapellaYAMLHandler:
    def __init__(self):
        self.file_name = None
        self.referenced_objects = []
        self.yaml_content = ""
        
    def get_yaml_content(self):
        """Returen the Yaml content created."""
        return self.yaml_content
    
    def write_output_file(self):
        """Generate a file capella_model.yaml"""
        self.file_name = "capella_model.yaml"
        # Initialize the file with a header
        with open(self.file_name, 'w') as f:
            f.write("# YAML file for Capella objects\n")
            f.write(self.yaml_content + "\n")

    def display(self):
        """Display the content of the yaml_content."""
        print(self.yaml_content)
 
    def generate_yaml_referenced_objects(self):
        """generate YAML content of referenced objects."""
        for ref_obj in self.referenced_objects:
                    self.generate_yaml(ref_obj) 
       
            
    def _track_referenced_objects(self, obj):
        """Track referenced objects to allow further expansion as primary objects."""
        if obj.__class__.__name__ ==  "LogicalComponent" :  
            for comp in obj.components:
                if comp not in self.referenced_objects:
                    self.referenced_objects.append(comp)
            for port in obj.ports:
                if port not in self.referenced_objects:
                    self.referenced_objects.append(port)
                for e in port.exchanges:
                    if e not in self.referenced_objects:
                        self.referenced_objects.append(e)
            for func in obj.allocated_functions:
                if func not in self.referenced_objects:
                    self.referenced_objects.append(func)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
                for pv in apvg.property_values:
                    if pv not in self.referenced_objects:
                        self.referenced_objects.append(pv)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con)
            for sm in obj.state_machines:
                if sm not in self.referenced_objects:
                    self.referenced_objects.append(sm)

        if obj.__class__.__name__ ==  "Entity" :  
            for ent in obj.entities:
                if ent not in self.referenced_objects:
                    self.referenced_objects.append(ent)
            for act in obj.activities:
                if act not in self.referenced_objects:
                    self.referenced_objects.append(act)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
                for pv in apvg.property_values:
                    if pv not in self.referenced_objects:
                        self.referenced_objects.append(pv)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con)
            for sm in obj.state_machines:
                if sm not in self.referenced_objects:
                    self.referenced_objects.append(sm)
        if obj.__class__.__name__  ==  "PhysicalComponent" and obj.nature  ==  "NODE":  
                for dc in obj.deployed_components:
                        if dc not in self.referenced_objects:
                            self.referenced_objects.append(dc)
                for physical_port in obj.physical_ports:
                    if physical_port not in self.referenced_objects:
                        self.referenced_objects.append(physical_port)
                    for link in physical_port.links:
                        if link not in self.referenced_objects:
                            self.referenced_objects.append(link)
                for apvg in obj.applied_property_value_groups:
                    if apvg not in self.referenced_objects:
                        self.referenced_objects.append(apvg)
                for apv in obj.applied_property_values:
                    if apv not in self.referenced_objects:
                        self.referenced_objects.append(apv)
                for con in obj.constraints:
                    if con not in self.referenced_objects:
                        self.referenced_objects.append(con)
        if obj.__class__.__name__  ==  "PhysicalComponent" and obj.nature  ==  "BEHAVIOR":  
                for dc in obj.deployed_components:
                        if dc not in self.referenced_objects:
                            self.referenced_objects.append(dc)
                for port in obj.ports:
                    if port not in self.referenced_objects:
                        self.referenced_objects.append(port)
                    for e in port.exchanges:
                        if e not in self.referenced_objects:
                            self.referenced_objects.append(e)
                    for func in obj.allocated_functions:
                        if func not in self.referenced_objects:
                            self.referenced_objects.append(func)
                    for apvg in obj.applied_property_value_groups:
                        if apvg not in self.referenced_objects:
                            self.referenced_objects.append(apvg)
                    for apv in obj.applied_property_values:
                        if apv not in self.referenced_objects:
                            self.referenced_objects.append(apv)
                    for con in obj.constraints:
                        if con not in self.referenced_objects:
                            self.referenced_objects.append(con)
        if obj.__class__.__name__ ==  "LogicalFunction" or obj.__class__.__name__ ==  "SystemFunction" or obj.__class__.__name__ ==  "PhysicalFunction":  
                    if obj.owner not in self.referenced_objects:
                            self.referenced_objects.append(obj.owner)
                    for port in obj.inputs:
                        if port not in self.referenced_objects:
                            self.referenced_objects.append(port)
                        for e in port.exchanges:
                            if e not in self.referenced_objects:
                                self.referenced_objects.append(e)
                    for port in obj.outputs:
                        if port not in self.referenced_objects:
                            self.referenced_objects.append(port)
                        for e in port.exchanges:
                            if e not in self.referenced_objects:
                                self.referenced_objects.append(e)
                    for apvg in obj.applied_property_value_groups:
                        if apvg not in self.referenced_objects:
                            self.referenced_objects.append(apvg)
                    for apv in obj.applied_property_values:
                        if apv not in self.referenced_objects:
                            self.referenced_objects.append(apv)
                    for con in obj.constraints:
                        if con not in self.referenced_objects:
                            self.referenced_objects.append(con)
        if obj.__class__.__name__ ==  "OperationalActivity" :  
                    if obj.owner not in self.referenced_objects:
                            self.referenced_objects.append(obj.owner)
                    for ain in obj.inputs:
                        if ain not in self.referenced_objects:
                            self.referenced_objects.append(ain)
                    for out in obj.outputs:
                        if out not in self.referenced_objects:
                            self.referenced_objects.append(out)
                    for apvg in obj.applied_property_value_groups:
                        if apvg not in self.referenced_objects:
                            self.referenced_objects.append(apvg)
                    for apv in obj.applied_property_values:
                        if apv not in self.referenced_objects:
                            self.referenced_objects.append(apv)
                    for con in obj.constraints:
                        if con not in self.referenced_objects:
                            self.referenced_objects.append(con)
        if obj.__class__.__name__ ==  "FunctionalChain" or obj.__class__.__name__ ==  "OperationalProcess" :  
            for inv in obj.involved:
                if inv not in self.referenced_objects:
                    self.referenced_objects.append(inv)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con) 
                    
        if obj.__class__.__name__ ==  "StateTransition" :  
            for eff in obj.effects:
                if eff not in self.referenced_objects:
                    self.referenced_objects.append(eff)
            for t in obj.triggers:
                if t not in self.referenced_objects:
                    self.referenced_objects.append(t)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con) 

        if obj.__class__.__name__ ==  "State" : 
            for og in obj.outgoing_transitions:
                if og not in self.referenced_objects:
                    self.referenced_objects.append(og)
            for inc in obj.incoming_transitions:
                if inc not in self.referenced_objects:
                    self.referenced_objects.append(inc)
            for da in obj.do_activity:
                if da not in self.referenced_objects:
                    self.referenced_objects.append(da)
            for en in obj.entries:
                if en not in self.referenced_objects:
                    self.referenced_objects.append(en)
            for ex in obj.exits:
                if ex not in self.referenced_objects:
                    self.referenced_objects.append(ex)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con) 
        if obj.__class__.__name__ ==  "InitialPseudoState" :  
            for og in obj.outgoing_transitions:
                if og not in self.referenced_objects:
                    self.referenced_objects.append(og)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con)       
        
        if obj.__class__.__name__ ==  "StateMachine" :  
            for region in obj.regions:
                for state in region.states:
                    if state not in self.referenced_objects:
                        self.referenced_objects.append(state)
                for transition in region.transitions:
                    if transition not in self.referenced_objects:
                        self.referenced_objects.append(transition)
            for apvg in obj.applied_property_value_groups:
                if apvg not in self.referenced_objects:
                    self.referenced_objects.append(apvg)
            for apv in obj.applied_property_values:
                if apv not in self.referenced_objects:
                    self.referenced_objects.append(apv)
            for con in obj.constraints:
                if con not in self.referenced_objects:
                    self.referenced_objects.append(con) 

        if obj.__class__.__name__ ==  "PropertyValueGroup" :  
                for apvg in obj.applied_property_value_groups:
                    if apvg not in self.referenced_objects:
                        self.referenced_objects.append(apvg)
                for apv in obj.applied_property_values:
                    if apv not in self.referenced_objects:
                        self.referenced_objects.append(apv)
                for con in obj.constraints:
                    if con not in self.referenced_objects:
                        self.referenced_objects.append(con) 
                for pvg in obj.property_value_groups:
                    if pvg not in self.referenced_objects:
                        self.referenced_objects.append(pvg)
                for pv in obj.property_values:
                    if pv not in self.referenced_objects:
                        self.referenced_objects.append(pv)
    
    def generate_yaml(self, obj):

        """Generate YAML for primary objects and manage references."""
        default_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""
        state_machine_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        regions:
        {% for region in regions %}
        - name: "{{ region.name }}"
          states:
          {% for state in region.states %}
            - name: "{{ state.name }}"
              ref_uuid : {{ state.uuid }}
          {% endfor %}
          transitions:
          {% for transition in region.transitions %}
            - name: "{{ transition.name }}"
              ref_uuid : {{ transition.uuid }}
          {% endfor %}
        {% endfor %}
"""     

        state_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        outgoing transtions:
        {% for og in outgoing_transitions %}
          - name: {{ og.name }}
            ref_uuid : {{ og.uuid }}
        {% endfor %}
        incoming transtions:
        {% for inc in incoming_transitions %}
          - name: {{ inc.name }}
            ref_uuid : {{ inc.uuid }}
        {% endfor %}
        functions:
        {% for func in functions %}
          - name: {{ func.name }}
            ref_uuid : {{ func.uuid }}
        {% endfor %}
        do functions:
        {% for da in do_activity %}
          - name: {{ da.name }}
            ref_uuid : {{ da.uuid }}
        {% endfor %}
        entry functions:
        {% for en in entries %}
          - name: {{ en.name }}
            ref_uuid : {{ en.uuid }}
        {% endfor %}
        exits functions:
        {% for ex in exits %}
          - name: {{ ex.name }}
            ref_uuid : {{ ex.uuid }}
        {% endfor %}
"""    
        psusdo_state_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        outgoing transtions:
        {% for og in outgoing_transitions %}
          - name: {{ og.name }}
            ref_uuid : {{ og.uuid }}
        {% endfor %}
"""   
        
        transition_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        guard: {{ guard }}
        triggers:
        {% for t in triggers %}
          - name: {{ t.name }}
            ref_uuid : {{ t.uuid }}
        {% endfor %}
        source state:
          - name: {{ source_name }}
            ref_uuid : {{ source_uuid }}
        destination state:
          - name: {{ dest_name }}
            ref_uuid : {{ dest_uuid }}
        after function:
        {% for ef in effects %}
          - name: {{ ef.name }}
            ref_uuid : {{ ef.uuid }}
        {% endfor %}

"""  
        
        function_exchange_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        source function:
            source_function_name: {{ source_function }}
            ref_uuid: {{ source_function_uuid }}
        target function:
            target_function_name: {{ target_function }}
            ref_uuid: {{ target_function_uuid }}
         {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""
        functional_chain_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        involved:
        {% for inv in involved %}
          - name: {{  inv.name }}
            ref_uuid: uuid : {{ inv.uuid }}
        {% endfor %}
         {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""



        
        property_value_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        value :  {{ value }}
"""
        property_value_group_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        property value groups:
        {% for pvg in property_value_groups %}
          - name: {{  apvg.name }}
            ref_uuid: uuid : {{ apvg.uuid }}
        {% endfor %}
        property values:
        {% for pv in property_values %}
          - name: {{  pv.name }}
            ref_uuid: uuid : {{ pv.uuid }}
        {% endfor %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        
""" 
        logical_component_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        is_human : {{ is_human }}
        components:
        {% for comp in components %}
          - component {{ comp.name }}
            ref_uuid : {{ comp.uuid }}
        {% endfor %}
        deployed components:
        {% for dc in deployed_components %}
          - deployed_behavior_component {{ dc.name }}
            ref_uuid : {{ dc.uuid }}
        {% endfor %}
        allocated functions:
        {% for func in allocated_functions %}
          - name: {{ func.name }}
            ref_uuid : {{ func.uuid }}
        {% endfor %}
        ports:
        {% for port in ports %}
          - name: {{ port.name }}
            description :  {{ port.description }}
            ref_uuid : {{ port.uuid }}
            exchanges:
            {% for exchange in port.exchanges %}
              - name: {{ exchange.name }}
                ref_uuid:  {{ exchange.uuid }}
                description :  {{ exchange.description }}
                source_component_name: {{ exchange.source_component }}
                ref__uuid: {{ exchange.source_component_uuid }}
                target_component_name: {{ exchange.target_component }}
                ref_uuid: {{ exchange.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
        {% if state_machines %}state machines:
            {% for sm in state_machines %}
              - name: {{  sm.name }}
                ref_uuid : {{ sm.uuid }}
            {% endfor %}
        {% endif %}
"""

        entity_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        is_human : {{ is_human }}
        is_actor : {{ is_actor }}
        entities:
        {% for ent in entities %}
          - component {{ ent.name }}
            ref_uuid : {{ ent.uuid }}
        {% endfor %}
        deployed components:
        allocated activities:
        {% for act in allocated_activities %}
          - name: {{ act.name }}
            ref_uuid : {{ act.uuid }}
        {% endfor %}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
        {% if state_machines %}state machines:
            {% for sm in state_machines %}
              - name: {{  sm.name }}
                ref_uuid : {{ sm.uuid }}
            {% endfor %}
        {% endif %}
"""
        node_component_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        is_human : {{ is_human }}
        deployed_components:
        {% for dc in deployed_components %}
          - deployed_behavior_component {{ dc.name }}
            ref_uuid : {{ dc.uuid }}
        {% endfor %}
        physical ports:
        {% for physical_port in physical_ports %}
          - name: {{ physical_port.name }}
            description :  {{ physical_port.description }}
            ref_uuid : {{ physical_port.uuid }}
            links:
            {% for link in physical_port.links %}
              - name: {{ link.name }}
                ref_uuid:  {{ link.uuid }}
                description :  {{ link.description }}
                source_component_name: {{ link.source_component }}
                ref__uuid: {{ link.source_component_uuid }}
                target_component_name: {{ link.target_component }}
                ref__uuid: {{ link.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""

        function_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        owner :
          - name : {{owner_name}}
            ref_uuid : {{owner_uuid}}
        child functions:
        {% for func in child_functions %}
          - name: {{ func.name }}
            ref_uuid : {{ func.uuid }}
        {% endfor %}
        inputs:
        {% for port in inputs %}
          - name: {{ port.name }}
            description :  {{ port.description }}
            ref_uuid : {{ port.uuid }}
            exchanges:
            {% for exchange in port.exchanges %}
              - name: {{ exchange.name }}
                ref_uuid:  {{ exchange.uuid }}
                description :  {{ exchange.description }}
                source_function_name: {{ exchange.source_component }}
                ref_uuid: {{ exchange.source_component_uuid }}
                target_function_name: {{ exchange.target_component }}
                ref_uuid: {{ exchange.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        outputs:
        {% for port in outputs %}
          - name: {{ port.name }}
            description :  {{ port.description }}
            ref_uuid : {{ port.uuid }}
            exchanges:
            {% for exchange in port.exchanges %}
              - name: {{ exchange.name }}
                ref_uuid:  {{ exchange.uuid }}
                description :  {{ exchange.description }}
                source_function_name: {{ exchange.source_component }}
                ref_uuid: {{ exchange.source_component_uuid }}
                target_function_name: {{ exchange.target_component }}
                ref_uuid: {{ exchange.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""

        activity_template = """
    {{type}}
      - name: {{ name }}
        primary_uuid: {{ uuid }}
        description : {{ description }}
        owner :
          - name : {{owner_name}}
            ref_uuid : {{owner_uuid}}
        child activities:
        {% for act in child_sctivities %}
          - name: {{ act.name }}
            ref_uuid : {{ act.uuid }}
        {% endfor %}
        inputs:
        {% for port in inputs %}
          - name: {{ port.name }}
            description :  {{ port.description }}
            ref_uuid : {{ port.uuid }}
            exchanges:
            {% for exchange in port.exchanges %}
              - name: {{ exchange.name }}
                ref_uuid:  {{ exchange.uuid }}
                description :  {{ exchange.description }}
                source_function_name: {{ exchange.source_component }}
                ref_uuid: {{ exchange.source_component_uuid }}
                target_function_name: {{ exchange.target_component }}
                ref_uuid: {{ exchange.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        outputs:
        {% for port in outputs %}
          - name: {{ port.name }}
            description :  {{ port.description }}
            ref_uuid : {{ port.uuid }}
            exchanges:
            {% for exchange in port.exchanges %}
              - name: {{ exchange.name }}
                ref_uuid:  {{ exchange.uuid }}
                description :  {{ exchange.description }}
                source_function_name: {{ exchange.source_component }}
                ref_uuid: {{ exchange.source_component_uuid }}
                target_function_name: {{ exchange.target_component }}
                ref_uuid: {{ exchange.target_component_uuid }}
            {% endfor %}
        {% endfor %}
        {% if applied_property_value_groups %}applied property value groups:
            {% for apvg in applied_property_value_groups %}
              - name: {{ apvg.name }}
                ref_uuid : {{ apvg.uuid }}
            {% endfor %}
        {% endif %}
        {% if applied_property_values %}applied property values:
            {% for apv in applied_property_values %}
              - name: {{ apv.name }}
                ref_uuid : {{ apv.uuid }}
            {% endfor %}
        {% endif %}
        {% if constraints %}constraints:
            {% for cons in constraints %}
              - name: {{ cons.name }}
                ref_uuid : {{ cons.uuid }}
            {% endfor %}
        {% endif %}
        {% if exchanges %}exchanges:
            {% for excs in exchanges %}
              - name: {{  e.name }}
                ref_uuid : {{ e.uuid }}
            {% endfor %}
        {% endif %}
"""
        # Build the data for the YAML generation
        #print("Type:", obj.__class__.__name__)
        if obj.__class__.__name__ ==  "LogicalComponent" :    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "is_human":obj.is_human,
                "description" :obj.description,
                "allocated_functions": [{"name": f.name , "uuid": f.uuid} for f in obj.allocated_functions],
                "ports": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description": e.description,"source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid} for e in getattr(p, 'exchanges', [])]
                         } for p in obj.ports],
                 "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                 "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                 "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints],
                 "state_machines": [{"name": sm.name, "uuid": sm.uuid} for sm in obj.state_machines]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(logical_component_template)

 
            self.yaml_content = self.yaml_content + template.render(data)

        # Build the data for the YAML generation
        elif obj.__class__.__name__ ==  "Entity" :    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "is human":obj.is_human,
                "is actor":obj.is_actor,
                "description" :obj.description,
                "allocated_activities": [{"name": a.name , "uuid": a.uuid} for a in obj.activities],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints],
                "state_machines": [{"name": sm.name, "uuid": sm.uuid} for sm in obj.state_machines]
            }
            #print(data)
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(entity_template)

 
            self.yaml_content = self.yaml_content + template.render(data)

        # Build the data for the YAML generation      
        elif obj.__class__.__name__ ==  "FunctionalChain" or obj.__class__.__name__ ==  "OperationalProcess":    
            data = {
                "type" : obj.__class__.__name__,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "involved": [{"name": inv.name , "uuid": inv.uuid} for inv in obj.involved],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(functional_chain_template)

 
            self.yaml_content = self.yaml_content + template.render(data)


# Build the data for the YAML generation
        
       
        elif obj.__class__.__name__ ==  "SystemFuntion" or obj.__class__.__name__ ==  "LogicalFunction" or obj.__class__.__name__ ==  "PhysicalFunction":    
            data = {
                "type" : obj.__class__.__name__,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "owner_name" :obj.owner.name,
                "owner_uuid" :obj.owner.uuid,
                "child_functions" :[{"name": func.name, "uuid": func.uuid} for func in obj.functions],
                "inputs": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description":e.description, "source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid  } for e in getattr(p, 'exchanges', [])]
                         } for p in obj.inputs],
                "outputs": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description":e.description, "source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid } for e in getattr(p, 'exchanges', [])]
                         } for p in obj.outputs],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(function_template)

 
            self.yaml_content = self.yaml_content + template.render(data)


        elif obj.__class__.__name__ ==  "OperationalActivity" : 
            data = {
                "type" : obj.__class__.__name__,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "owner_name" :obj.owner.name,
                "owner_uuid" :obj.owner.uuid,
                "child activities" :[{"name": func.name, "uuid": func.uuid} for func in obj.activities],
                "inputs": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description":e.description, "source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid  } for e in getattr(p, 'exchanges', [])]
                         } for p in obj.inputs],
                "outputs": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description":e.description, "source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid } for e in getattr(p, 'exchanges', [])]
                         } for p in obj.outputs],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(activity_template)

 
            self.yaml_content = self.yaml_content + template.render(data)
# Build the data for the YAML generation
        
        elif obj.__class__.__name__ ==  "FunctionalExchange" :    
            data = {
                "type" : obj.__class__.__name__,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "source_function": obj.source.owner.name,
                "source_function_uuid": obj.source.owner.uuid,
                "target_function": obj.target.owner.name, 
                "target_function_uuid": obj.target.owner.uuid ,
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(function_exchange_template)

 
            self.yaml_content = self.yaml_content + template.render(data)

        elif obj.__class__.__name__  ==  "PhysicalComponent" and obj.nature  ==  "NODE":  
                data = {
                    "type" : obj.__class__.__name__,
                    "parent_uuid": obj.parent.uuid if obj.parent else None,
                    "name": obj.name,
                    "uuid" : obj.uuid,
                    "is_human":obj.is_human,
                    "description" :obj.description,
                    "deployed_components": [{"name": dc.name , "uuid": dc.uuid} for dc in obj.deployed_components],
                    "physical_ports": [{
                        "name": p.name,
                        "uuid": p.uuid,
                        "description": p.description,
                        "links": [{"name": link.name, "uuid": link.uuid, "description": link.description,"source_component": link.source.owner.name, "source_component_uuid": link.source.owner.uuid, "target_component": link.target.owner.name, "target_component_uuid": link.target.owner.uuid} for link in p.links]
                             } for p in obj.physical_ports],
                     "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                     "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                     "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
                }
                # Add referenced objects for expansion
                self._track_referenced_objects(obj)
        
                # Render the template
                template = Template(node_component_template)
                self.yaml_content = self.yaml_content + template.render(data)
                
               
        elif obj.__class__.__name__  ==  "PhysicalComponent" and obj.nature  ==  "BEHAVIOR":  
                data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "is_human":obj.is_human,
                "description" :obj.description,
                "deployed_components": [{"name": dc.name , "uuid": dc.uuid} for dc in obj.deployed_components],
                "allocated_functions": [{"name": f.name , "uuid": f.uuid} for f in obj.allocated_functions],
                "ports": [{
                    "name": p.name,
                    "uuid": p.uuid,
                    "description": p.description,
                    "exchanges": [{"name": e.name, "uuid": e.uuid, "description": e.description,"source_component": e.source.owner.name, "source_component_uuid": e.source.owner.uuid, "target_component": e.target.owner.name, "target_component_uuid": e.target.owner.uuid} for e in getattr(p, 'exchanges', [])]
                         } for p in obj.ports],
                 "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                 "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                 "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
                }
        
                # Add referenced objects for expansion
                self._track_referenced_objects(obj)
        
                # Render the template
                template = Template(logical_component_template)
                self.yaml_content = self.yaml_content + template.render(data)
                
              


                
        elif obj.__class__.__name__ ==  "StringPropertyValue"  or obj.__class__.__name__ ==  "FloatPropertyValue":    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "value" : obj.value,
                "description" :obj.description,
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid ,"value": pv.value } for apv in obj.applied_property_values],
                "property_values": [{"name": pv.name, "uuid": pv.uuid , "value": pv.value} for pv in obj.property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(property_value_template)
            #print(template)
            #print(data)
            self.yaml_content = self.yaml_content +  template.render(data)
            
          
            

        elif obj.__class__.__name__ ==  "PropertyValueGroup" :    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "property_value_groups": [{"name": pvg.name, "uuid": pvg.uuid} for pvg in obj.property_value_groups],
                "property_values": [{"name": pv.name, "uuid": pv.uuid} for pv in obj.property_values],
               
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(property_value_group_template)
            self.yaml_content = self.yaml_content + template.render(data)
            
        elif obj.__class__.__name__ ==  "StateMachine" :   
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "regions": [{
                    "name": region.name,
                    "uuid": region.uuid,
                    "description": region.description,
                    "states": [{"name": s.name, "uuid": s.uuid, "description": s.description} 
                        for s in getattr(region, 'states', [])],      
                    "transitions": [{"name": t.name, "uuid": t.uuid, "description": t.description} 
                               for t in getattr(region, 'transitions', [])],
                
                    } for region in obj.regions],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "property_value_groups": [{"name": pvg.name, "uuid": pvg.uuid} for pvg in obj.property_value_groups],
                "property_values": [{"name": pv.name, "uuid": pv.uuid} for pv in obj.property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(state_machine_template)
            self.yaml_content = self.yaml_content + template.render(data)

        elif obj.__class__.__name__ ==  "State" :  
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "outgoing_transitions": [{"name": og.name, "uuid": og.uuid} for og in obj.outgoing_transitions],
                "incoming_transitions": [{"name": inc.name, "uuid": inc.uuid} for inc in obj.incoming_transitions],
                "do activites": [{"name": da.name, "uuid": da.uuid} for da in obj.do_activity],
                "exits": [{"name": ex.name, "uuid": ex.uuid} for ex in obj.exits],
                "entries": [{"name": en.name, "uuid": en.uuid} for en in obj.entries],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "property_value_groups": [{"name": pvg.name, "uuid": pvg.uuid} for pvg in obj.property_value_groups],
                "property_values": [{"name": pv.name, "uuid": pv.uuid} for pv in obj.property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid,"value": cons.value} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(state_template)
            self.yaml_content = self.yaml_content + template.render(data)           
        elif obj.__class__.__name__ ==  "InitialPseudoState" :    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "outgoing_transitions": [{"name": og.name, "uuid": og.uuid} for og in obj.outgoing_transitions],
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "property_value_groups": [{"name": pvg.name, "uuid": pvg.uuid} for pvg in obj.property_value_groups],
                "property_values": [{"name": pv.name, "uuid": pv.uuid} for pv in obj.property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid,"value": cons.value} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(psusdo_state_template)
            self.yaml_content = self.yaml_content + template.render(data)           

        
        elif obj.__class__.__name__ ==  "StateTransition" :    
            data = {
                "type" : obj.__class__.__name__,
                "parent_uuid": obj.parent.uuid if obj.parent else None,
                "name": obj.name,
                "uuid" : obj.uuid,
                "description" :obj.description,
                "source" :obj.source,
                "triggers": [{"name": t.name, "uuid": t.uuid} for t in obj.triggers],
                "effects": [{"name": ef.name, "uuid": ef.uuid} for ef in obj.effects],
                "source_name":  obj.source.name,
                "source_uuid":  obj.source.uuid,
                "dest_name":  obj.destination.name,
                "dest_uuid":  obj.destination.uuid,
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "property_value_groups": [{"name": pvg.name, "uuid": pvg.uuid} for pvg in obj.property_value_groups],
                "property_values": [{"name": pv.name, "uuid": pv.uuid} for pv in obj.property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
    
            # Add referenced objects for expansion
            self._track_referenced_objects(obj)
    
            # Render the template
            template = Template(transition_template)
            self.yaml_content = self.yaml_content + template.render(data)           
                      
        
        else :
            print(obj.name, "is be formatted with default properties, its type", obj.__class__.__name__," is not supported with tailored processiong.")
            #print(obj)
            data = {
                "type" : obj.__class__.__name__,
                "name": obj.name,
                "uuid":obj.uuid,
                "description" :obj.description,
                "applied_property_value_groups": [{"name": apvg.name, "uuid": apvg.uuid} for apvg in obj.applied_property_value_groups],
                "applied_property_values": [{"name": apv.name, "uuid": apv.uuid} for apv in obj.applied_property_values],
                "constraints": [{"name": cons.name, "uuid": cons.uuid} for cons in obj.constraints]
            }
            # Render the template
            template = Template(default_template)
            self.yaml_content = self.yaml_content + template.render(data)

        
    


