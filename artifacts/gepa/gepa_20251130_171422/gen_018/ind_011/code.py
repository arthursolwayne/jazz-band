
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, rhythmic variation, and space
drum_notes = [
    (0.0, 38, 80),       # snare on 2
    (0.75, 42, 60),      # hihat on 3
    (1.25, 42, 60),      # hihat on 4
    (1.375, 36, 70),     # kick on 4
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (D, F#, A, D)
sax_notes = [
    (1.5, 62, 100, 0.5),  # D4
    (2.0, 67, 90, 0.25),  # F#4
    (2.25, 69, 95, 0.25), # A4
    (2.5, 62, 100, 0.25), # D4
    (2.75, 67, 95, 0.25), # F#4
    (3.0, 69, 100, 0.25), # A4
    (3.25, 62, 100, 0.25), # D4
    (3.5, 67, 95, 0.25),  # F#4
    (3.75, 69, 100, 0.25), # A4
    (4.0, 62, 100, 0.5),  # D4
]

for time, note, velocity, duration in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    sax.notes.append(n)

# Bass line: walking with chromatic approaches
bass_notes = [
    (1.5, 62, 80, 0.5),   # D4
    (2.0, 63, 85, 0.5),   # Eb4
    (2.5, 67, 80, 0.5),   # F#4
    (3.0, 69, 85, 0.5),   # A4
    (3.5, 67, 80, 0.5),   # F#4
    (4.0, 65, 85, 0.5),   # G#4
    (4.5, 69, 80, 0.5),   # A4
    (5.0, 67, 85, 0.5),   # F#4
    (5.5, 62, 80, 0.5),   # D4
]

for time, note, velocity, duration in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    bass.notes.append(n)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    (1.75, 64, 80, 0.25), # C7
    (1.75, 67, 80, 0.25), # E7
    (1.75, 69, 80, 0.25), # G7
    (1.75, 71, 80, 0.25), # Bb7
    # Bar 3 (2.5 - 3.0)
    (2.75, 64, 80, 0.25), # C7
    (2.75, 67, 80, 0.25), # E7
    (2.75, 69, 80, 0.25), # G7
    (2.75, 71, 80, 0.25), # Bb7
    # Bar 4 (3.5 - 4.0)
    (3.75, 64, 80, 0.25), # C7
    (3.75, 67, 80, 0.25), # E7
    (3.75, 69, 80, 0.25), # G7
    (3.75, 71, 80, 0.25), # Bb7
]

for time, note, velocity, duration in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    piano.notes.append(n)

# Drums in bars 2-4: full energy, fills, and syncopation
drum_notes = [
    # Bar 2 (1.5 - 2.0)
    (1.5, 36, 90),       # kick on 1
    (1.75, 38, 95),      # snare on 2
    (2.0, 42, 80),       # hihat on 3
    (2.0, 42, 80),       # hihat on 3
    (2.25, 42, 80),      # hihat on 4
    (2.25, 36, 95),      # kick on 4
    # Bar 3 (2.5 - 3.0)
    (2.5, 36, 90),       # kick on 1
    (2.75, 38, 95),      # snare on 2
    (3.0, 42, 80),       # hihat on 3
    (3.0, 42, 80),       # hihat on 3
    (3.25, 42, 80),      # hihat on 4
    (3.25, 36, 95),      # kick on 4
    # Bar 4 (3.5 - 4.0)
    (3.5, 36, 90),       # kick on 1
    (3.75, 38, 95),      # snare on 2
    (4.0, 42, 80),       # hihat on 3
    (4.0, 42, 80),       # hihat on 3
    (4.25, 42, 80),      # hihat on 4
    (4.25, 36, 95),      # kick on 4
    # Fill before end
    (5.0, 36, 80),       # kick
    (5.125, 38, 90),     # snare
    (5.25, 42, 100),     # hihat
    (5.375, 42, 100),    # hihat
    (5.5, 42, 100),      # hihat
    (5.625, 38, 90),     # snare
    (5.75, 42, 100),     # hihat
    (5.875, 42, 100),    # hihat
    (6.0, 36, 90)        # kick
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
