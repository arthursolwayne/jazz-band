
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36),  # Kick on 1
    (0.375, 42), # Hihat on 2
    (0.75, 38),  # Snare on 2
    (1.125, 42), # Hihat on 3
    (1.5, 36),   # Kick on 3
    (1.875, 42), # Hihat on 4
    (2.25, 38),  # Snare on 4
    (2.625, 42)  # Hihat on 4
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (1.5, 72),  # F3
    (1.875, 73), # F#3 (chromatic approach)
    (2.25, 71),  # E3
    (2.625, 69), # D3
    (3.0, 67),   # C3
    (3.375, 68), # C#3
    (3.75, 65),  # Bb2
    (4.125, 64), # Bb2
    (4.5, 67),   # C3
    (4.875, 69), # D3
    (5.25, 71),  # E3
    (5.625, 72)  # F3
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comping
# Bars 2-4: F7, Bb7, E7, A7
piano_notes = [
    # Bar 2
    (1.875, 65), # F7 (F, A, C, E)
    (1.875, 69), # F7
    (1.875, 72), # F7
    (1.875, 76), # F7
    # Bar 3
    (3.375, 60), # Bb7 (Bb, D, F, Ab)
    (3.375, 64), # Bb7
    (3.375, 67), # Bb7
    (3.375, 71), # Bb7
    # Bar 4
    (4.875, 64), # E7 (E, G#, B, D)
    (4.875, 68), # E7
    (4.875, 71), # E7
    (4.875, 74), # E7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: Motif - F, Ab, Bb, F (one short motif, make it sing)
sax_notes = [
    (1.5, 72),  # F4
    (1.875, 76), # Ab4
    (2.25, 71),  # Bb4
    (2.625, 72), # F4
    (3.0, 72),   # F4 (reprise)
    (3.375, 76), # Ab4
    (3.75, 71),  # Bb4
    (4.125, 72), # F4
    (4.5, 72),   # F4
    (4.875, 76), # Ab4
    (5.25, 71),  # Bb4
    (5.625, 72)  # F4
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
