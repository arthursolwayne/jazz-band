
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
    (0.0, 36), # Kick on 1
    (0.375, 42), # Hihat
    (0.75, 38), # Snare on 2
    (1.125, 42), # Hihat
    (1.5, 36), # Kick on 3
    (1.875, 42), # Hihat
    (2.25, 38), # Snare on 4
    (2.625, 42), # Hihat
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62), # D4
    (1.75, 63), # Eb4
    (2.0, 64), # E4
    (2.25, 65), # F4
    (2.5, 67), # G4
    (2.75, 69), # A4
    (3.0, 71), # Bb4
    (3.25, 72), # B4
    (3.5, 74), # C5
    (3.75, 76), # Db5
    (4.0, 77), # D5
    (4.25, 79), # Eb5
    (4.5, 81), # E5
    (4.75, 83), # F5
    (5.0, 85), # G5
    (5.25, 87), # A5
    (5.5, 89), # Bb5
    (5.75, 91), # B5
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),
    # Bar 3: Bm7b5 (B, D, F#, A)
    (3.0, 69), (3.0, 74), (3.0, 79), (3.0, 84),
    # Bar 4: G7 (G, B, D, F)
    (4.5, 67), (4.5, 72), (4.5, 77), (4.5, 81),
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67), # G4
    (1.75, 72), # B4
    (2.0, 67), # G4
    (2.25, 62), # D4
    (2.5, 67), # G4
    (2.75, 72), # B4
    (3.0, 77), # C5
    (3.25, 72), # B4
    (3.5, 74), # Db5
    (3.75, 77), # C5
    (4.0, 79), # Eb5
    (4.25, 77), # C5
    (4.5, 72), # B4
    (4.75, 67), # G4
    (5.0, 62), # D4
    (5.25, 67), # G4
    (5.5, 72), # B4
    (5.75, 72), # B4
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
