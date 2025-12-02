
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (1.5, 64), (1.875, 62), (2.25, 60), (2.625, 62),
    (3.0, 61), (3.375, 62), (3.75, 64), (4.125, 62),
    (4.5, 60), (4.875, 62), (5.25, 64), (5.625, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (2.25, 71), (2.25, 74), (2.25, 76), (2.25, 70),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.75, 67), (3.75, 70), (3.75, 76), (3.75, 71),
    # Bar 4: F7 again
    (5.25, 71), (5.25, 74), (5.25, 76), (5.25, 70)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax melody - short motif: F, Gb, Ab, A (bar 2), then repeat with variation (bar 4)
sax_notes = [
    # Bar 2: F, Gb, Ab, A
    (1.5, 71), (1.875, 70), (2.25, 69), (2.625, 71),
    # Bar 3: leave it hanging
    # Bar 4: F, Gb, Ab, Bb (variation)
    (4.5, 71), (4.875, 70), (5.25, 69), (5.625, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
