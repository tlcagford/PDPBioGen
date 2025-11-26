#!/usr/bin/env python3
"""
IMMEDIATE LAB DEPLOYMENT SCRIPT
Run this to initialize the complete quantum biological BCI system
"""

async def main():
    print("🚀 INITIALIZING QUANTUM BIOLOGICAL BCI LAB SYSTEM...")
    
    # 1. Initialize core system
    quantum_bci = QuantumBioBCI()
    print("✓ Quantum-BCI engine initialized")
    
    # 2. Initialize laboratory hardware
    await quantum_bci.lab_interface.initialize_hardware()
    print("✓ Laboratory hardware initialized")
    
    # 3. Run system validation
    validator = LabValidationProtocol(quantum_bci)
    validation_results = await validator.run_full_validation()
    print(f"✓ System validation completed: {validation_results['overall_score']:.2f}")
    
    # 4. Start real-time monitoring
    controller = ClosedLoopHealingController(quantum_bci)
    print("✓ Closed-loop controller ready")
    
    # 5. Begin experimental session
    print("🎯 STARTING QUANTUM HEALING SESSION...")
    session_results = await controller.run_healing_session(duration_minutes=30)
    
    print("✅ SESSION COMPLETED")
    print(f"   Quantum states recorded: {len(session_results['quantum_states'])}")
    print(f"   Interventions applied: {len(session_results['interventions'])}")
    print(f"   Final healing correlation: {session_results['quantum_states'][-1].healing_correlation:.3f}")

if __name__ == "__main__":
    asyncio.run(main())
