
import pretty_midi

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64, is_drum=False)  # Tenor sax
midi.instruments.append(instrument)

# Time resolution: 1/16 note = 0.1875 seconds (since 160 BPM = 0.375s per beat, 16 notes per beat)
# 4 bars = 6.0 seconds
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds
# 1 sixteenth note = 0.09375 seconds

def add_note(note, time, duration, velocity=100):
    instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_program = pretty_midi.Instrument(program=10, is_drum=True)
midi.instruments.append(drum_program)

# Bar 1 (0.0 to 1.5 seconds)
# Time in seconds: 0.0, 0.375, 0.75, 1.125, 1.5
# Kick on 1 (0.0) and 3 (0.75)
add_note(36, 0.0, 0.1875, velocity=100)  # Kick
add_note(36, 0.75, 0.1875, velocity=100)  # Kick

# Snare on 2 (0.375) and 4 (1.125)
add_note(38, 0.375, 0.1875, velocity=100)  # Snare
add_note(38, 1.125, 0.1875, velocity=100)  # Snare

# Hihat on every eighth
add_note(42, 0.0, 0.09375, velocity=80)
add_note(42, 0.09375, 0.09375, velocity=80)
add_note(42, 0.1875, 0.09375, velocity=80)
add_note(42, 0.28125, 0.09375, velocity=80)
add_note(42, 0.375, 0.09375, velocity=80)
add_note(42, 0.46875, 0.09375, velocity=80)
add_note(42, 0.5625, 0.09375, velocity=80)
add_note(42, 0.65625, 0.09375, velocity=80)
add_note(42, 0.75, 0.09375, velocity=80)
add_note(42, 0.84375, 0.09375, velocity=80)
add_note(42, 0.9375, 0.09375, velocity=80)
add_note(42, 1.03125, 0.09375, velocity=80)
add_note(42, 1.125, 0.09375, velocity=80)
add_note(42, 1.21875, 0.09375, velocity=80)
add_note(42, 1.3125, 0.09375, velocity=80)
add_note(42, 1.40625, 0.09375, velocity=80)

# Bar 2: Everyone in
# Key: F minor (F, Ab, Bb, C, Eb, Gb, A)
# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> open voicing
# Diane plays on 2 and 4
# Time: 1.5s to 3.0s
diane_program = pretty_midi.Instrument(program=0, is_drum=False)
midi.instruments.append(diane_program)

# Diane's chord: Fm7 (F, Ab, C, Eb)
# Root F (65), Ab (69), C (60), Eb (62)
add_note(65, 1.5, 0.1875, velocity=100)
add_note(69, 1.5, 0.1875, velocity=100)
add_note(60, 1.5, 0.1875, velocity=100)
add_note(62, 1.5, 0.1875, velocity=100)

# Marcus on bass: walking line (D2-G2), roots and fifths with chromatic approaches
# Time: 1.5s to 3.0s
# Fm7: F (65), C (60), Bb (57), Ab (69), D (50)
marcus_program = pretty_midi.Instrument(program=33, is_drum=False)
midi.instruments.append(marcus_program)

# Walking line in Fm: F, Bb, C, Ab, F, Bb, C, Ab
add_note(65, 1.5, 0.1875, velocity=100)
add_note(57, 1.75, 0.1875, velocity=100)
add_note(60, 2.0, 0.1875, velocity=100)
add_note(69, 2.25, 0.1875, velocity=100)
add_note(65, 2.5, 0.1875, velocity=100)
add_note(57, 2.75, 0.1875, velocity=100)
add_note(60, 3.0, 0.1875, velocity=100)
add_note(69, 3.25, 0.1875, velocity=100)

# Little Ray continues on 2 and 4
# Bar 2: 1.5s to 3.0s
add_note(36, 1.5, 0.1875, velocity=100)  # Kick
add_note(38, 1.875, 0.1875, velocity=100)  # Snare
add_note(36, 2.25, 0.1875, velocity=100)  # Kick
add_note(38, 2.625, 0.1875, velocity=100)  # Snare

add_note(42, 1.5, 0.09375, velocity=80)
add_note(42, 1.59375, 0.09375, velocity=80)
add_note(42, 1.6875, 0.09375, velocity=80)
add_note(42, 1.78125, 0.09375, velocity=80)
add_note(42, 1.875, 0.09375, velocity=80)
add_note(42, 1.96875, 0.09375, velocity=80)
add_note(42, 2.0625, 0.09375, velocity=80)
add_note(42, 2.15625, 0.09375, velocity=80)
add_note(42, 2.25, 0.09375, velocity=80)
add_note(42, 2.34375, 0.09375, velocity=80)
add_note(42, 2.4375, 0.09375, velocity=80)
add_note(42, 2.53125, 0.09375, velocity=80)
add_note(42, 2.625, 0.09375, velocity=80)
add_note(42, 2.71875, 0.09375, velocity=80)
add_note(42, 2.8125, 0.09375, velocity=80)
add_note(42, 2.90625, 0.09375, velocity=80)

# Bar 3: Tenor sax (you) — motif: start it, leave it hanging
# Time: 3.0s to 4.5s
# Start with a short phrase that feels like a question
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Use F, Ab, Bb, F — a "suspended" idea, then leave it hanging

add_note(65, 3.0, 0.09375, velocity=110)  # F
add_note(69, 3.1875, 0.09375, velocity=110)  # Ab
add_note(67, 3.375, 0.09375, velocity=110)  # Bb
add_note(65, 3.5625, 0.09375, velocity=110)  # F

# Bar 4: Resolution — Diane resolves, Marcus continues, Little Ray fills
# Diane: Gm7 (G, Bb, D, F)
add_note(67, 3.0, 0.1875, velocity=100)  # G
add_note(62, 3.0, 0.1875, velocity=100)  # F
add_note(65, 3.0, 0.1875, velocity=100)  # D
add_note(69, 3.0, 0.1875, velocity=100)  # Bb

# Marcus: C (60) on the downbeat (4.5s)
add_note(60, 4.5, 0.1875, velocity=100)

# Little Ray: Kick on 1 (3.0s), snare on 2 (3.375s), kick on 3 (3.75s), snare on 4 (4.125s)
add_note(36, 3.0, 0.1875, velocity=100)
add_note(38, 3.375, 0.1875, velocity=100)
add_note(36, 3.75, 0.1875, velocity=100)
add_note(38, 4.125, 0.1875, velocity=100)

# Hihat on every 8th
add_note(42, 3.0, 0.09375, velocity=80)
add_note(42, 3.09375, 0.09375, velocity=80)
add_note(42, 3.1875, 0.09375, velocity=80)
add_note(42, 3.28125, 0.09375, velocity=80)
add_note(42, 3.375, 0.09375, velocity=80)
add_note(42, 3.46875, 0.09375, velocity=80)
add_note(42, 3.5625, 0.09375, velocity=80)
add_note(42, 3.65625, 0.09375, velocity=80)
add_note(42, 3.75, 0.09375, velocity=80)
add_note(42, 3.84375, 0.09375, velocity=80)
add_note(42, 3.9375, 0.09375, velocity=80)
add_note(42, 4.03125, 0.09375, velocity=80)
add_note(42, 4.125, 0.09375, velocity=80)
add_note(42, 4.21875, 0.09375, velocity=80)
add_note(42, 4.3125, 0.09375, velocity=80)
add_note(42, 4.40625, 0.09375, velocity=80)

# Write the MIDI file
midi.write('4_bar_intro.mid')
