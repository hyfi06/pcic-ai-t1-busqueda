from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def load_alarm_model():
    alarma = BayesianNetwork([
        ('B', 'A'),  # Burglary -> Alarm
        ('E', 'A'),  # Earthqk -> Alarm
        ('A', 'J'),  # Alarm -> John calls
        ('A', 'M'),  # Mary
    ])

    cpd_burglary = TabularCPD(
        # +-------+-------+
        # | B(-b) | 0.999 |
        # +-------+-------+
        # | B(+b) | 0.001 |
        # +-------+-------+
        variable='B',
        variable_card=2,
        values=[
            [0.999],  # -b
            [0.001]  # +b
        ],
        state_names={'B': ['-b', '+b']}
    )

    cpd_earthqk = TabularCPD(
        # +-------+-------+
        # | E(-e) | 0.998 |
        # +-------+-------+
        # | E(+e) | 0.002 |
        # +-------+-------+
        variable='E',
        variable_card=2,
        values=[
            [0.998],  # -e
            [0.002]  # +e
        ],
        state_names={'E': ['-e', '+e']}
    )

    cpd_alarm = TabularCPD(
        # +-------+-------+-------+-------+-------+
        # | B     | B(-b) | B(-b) | B(+b) | B(+b) |
        # +-------+-------+-------+-------+-------+
        # | E     | E(-e) | E(+e) | E(-e) | E(+e) |
        # +-------+-------+-------+-------+-------+
        # | A(-a) | 0.999 | 0.71  | 0.06  | 0.05  |
        # +-------+-------+-------+-------+-------+
        # | A(+a) | 0.001 | 0.29  | 0.94  | 0.95  |
        # +-------+-------+-------+-------+-------+
        variable='A',
        variable_card=2,
        values=[
            #  -b    -b    +b   +b
            #  -e    +e    -e   -e
            [0.999, 0.71, 0.06, 0.05],  # -a
            [0.001, 0.29, 0.94, 0.95]  # +a
        ],
        evidence=['B', 'E'],
        evidence_card=[2, 2],
        state_names={
            'A': ['-a', '+a'],
            'B': ['-b', '+b'],
            'E': ['-e', '+e']
        }
    )

    cpd_john = TabularCPD(
        # +-------+-------+-------+
        # | A     | A(-a) | A(+a) |
        # +-------+-------+-------+
        # | J(-j) | 0.95  | 0.1   |
        # +-------+-------+-------+
        # | J(+j) | 0.05  | 0.9   |
        # +-------+-------+-------+
        variable='J',
        variable_card=2,
        values=[
            # -a  +a
            [0.95, 0.1],  # -j
            [0.05, 0.9]  # +j
        ],
        evidence=['A'],
        evidence_card=[2],
        state_names={
            'J': ['-j', '+j'],
            'A': ['-a', '+a']
        }
    )

    cpd_mary = TabularCPD(
        # +-------+-------+-------+
        # | A     | A(-a) | A(+a) |
        # +-------+-------+-------+
        # | M(-m) | 0.99  | 0.3   |
        # +-------+-------+-------+
        # | M(+m) | 0.01  | 0.7   |
        # +-------+-------+-------+
        variable='M',
        variable_card=2,
        values=[
            # -a  +a
            [0.99, 0.3],  # -j
            [0.01, 0.7]  # +j
        ],
        evidence=['A'],
        evidence_card=[2],
        state_names={
            'M': ['-m', '+m'],
            'A': ['-a', '+a']
        }
    )

    alarma.add_cpds(cpd_burglary, cpd_earthqk, cpd_alarm, cpd_john, cpd_mary)
    assert alarma.check_model()
    return alarma


def main():
    model = load_alarm_model()
    infer = VariableElimination(model)
    print('P(Burglary | JohnCalls=+j, MaryCalls=+m):')
    query_result = infer.query(
        variables=['B'],
        evidence={
            'J': '+j', 'M': '+m'
        }
    )
    print(query_result, end='\n\n')

    print('P(Earthqk | JohnCalls=+j, MaryCalls=+m):')
    query_result = infer.query(
        variables=['E'],
        evidence={
            'J': '+j', 'M': '+m'
        }
    )
    print(query_result, end='\n\n')

    print('P(JohnCalls | MaryCalls=-m):')
    query_result = infer.query(
        variables=['J'],
        evidence={
            'M': '-m'
        }
    )
    print(query_result, end='\n\n')

    print('Están d-separados de "Burglary" al observar "Alarm": ', end='')
    print(model.active_trail_nodes('B', observed='A'))


if __name__ == "__main__":
    main()
