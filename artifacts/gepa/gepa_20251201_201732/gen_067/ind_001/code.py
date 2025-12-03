
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Key signature: D minor (key number 10, which is D minor)
pm.key_signature_changes = [pretty_midi.KeySignature(10, 0.0)]

# Create instruments
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')

sax = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [sax, bass, piano, drums]

# Time per bar: 6.0 seconds / 4 bars = 1.5 seconds per bar
# Tempo = 160 BPM → 60/160 = 0.375 seconds per beat → 1.5 seconds per bar
# Beats per bar = 4
# Each beat = 0.375 seconds

# --- DRUMS: Little Ray (Bar 1)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(instrument, start_time, duration):
    # Kick on 1 and 3
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.05))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 0.80))
    
    # Snare on 2 and 4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.425))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.175))
    
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start_time + i * 0.375
        instrument.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05))

add_drums(drums, 0.0, 1.5)

# --- BASS: Marcus (Bar 1)
# Walking line: D2-G2, roots and fifths with chromatic approaches
def add_bass(instrument, start_time, duration):
    # D2 is MIDI 38, G2 is MIDI 43
    # Build a walking line with chromatic approaches
    # Bar 1: D2 (38) -> Eb2 (39) -> G2 (43) -> F2 (41)
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time, end=start_time + 0.375))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=start_time + 0.375, end=start_time + 0.75))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=start_time + 0.75, end=start_time + 1.125))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=start_time + 1.125, end=start_time + 1.5))

add_bass(bass, 0.0, 1.5)

# --- PIANO: Diane (Bar 1-4)
# Open voicings, resolve on the last bar
def add_piano(instrument, start_time, duration):
    # Bar 1: Dm7 (D, F, A, C) open voicing
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start_time, end=start_time + 0.75))  # D4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=start_time, end=start_time + 0.75))  # F4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start_time, end=start_time + 0.75))  # A4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start_time, end=start_time + 0.75))  # C4

    # Bar 2: G7 (G, B, D, F) open voicing
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start_time + 0.75, end=start_time + 1.5))  # G4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start_time + 0.75, end=start_time + 1.5))  # B4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start_time + 0.75, end=start_time + 1.5))  # D5
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=start_time + 0.75, end=start_time + 1.5))  # F4

    # Bar 3: Cm7 (C, Eb, G, Bb) open voicing
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start_time + 1.5, end=start_time + 2.25))  # C4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=start_time + 1.5, end=start_time + 2.25))  # Eb4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start_time + 1.5, end=start_time + 2.25))  # G4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=start_time + 1.5, end=start_time + 2.25))  # Bb4

    # Bar 4: F7 (F, A, C, Eb) open voicing
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=start_time + 2.25, end=start_time + 3.0))  # F4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=start_time + 2.25, end=start_time + 3.0))  # A4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start_time + 2.25, end=start_time + 3.0))  # C4
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=start_time + 2.25, end=start_time + 3.0))  # Eb4)

add_piano(piano, 0.0, 3.0)

# --- SAX: Dante (Bars 2-4)
# Melody: One short motif, haunting and memorable
def add_sax(instrument, start_time, duration):
    # Bar 2: Start with a D (MIDI 62) on beat 1
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + 0.25))
    # Bar 2: Ascend to F (65) on beat 2, hold a bit
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start_time + 0.375, end=start_time + 1.0))
    # Bar 3: Descend to C (60) on beat 1
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=start_time + 1.5, end=start_time + 1.75))
    # Bar 3: Ascend to D (62) on beat 2
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start_time + 1.875, end=start_time + 2.25))
    # Bar 4: Descend to Bb (59) on beat 3
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=59, start=start_time + 2.625, end=start_time + 2.875))
    # Bar 4: End on C (60), leaving it hanging
    instrument.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=start_time + 3.0, end=start_time + 3.25))

add_sax(sax, 1.5, 1.5)

# Save MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
