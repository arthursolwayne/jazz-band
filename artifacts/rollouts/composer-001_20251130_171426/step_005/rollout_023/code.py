
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # Bar 1
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # Bar 3
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches, no repeating notes)
# F7 chord: F, A, C, E
# Walking line: F, G#, A, Bb, B, C, D, Eb, E, F#, G, Ab, A, Bb, B, C
bass_notes = [
    (1.5, 77), (1.875, 80), (2.25, 82), (2.625, 81),  # F, G#, A, Bb
    (3.0, 83), (3.375, 84), (3.75, 87), (4.125, 85),  # B, C, D, Eb
    (4.5, 86), (4.875, 88), (5.25, 89), (5.625, 87)   # E, F#, G, Ab
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Diane - Piano (7th chords, comp on 2 and 4)
# F7: F, A, C, E
# Comp on 2 and 4 of bars 2, 3, 4
piano_notes = [
    (2.25, 77), (2.25, 82), (2.25, 79), (2.25, 86),  # F7 on beat 2 of bar 2
    (3.75, 77), (3.75, 82), (3.75, 79), (3.75, 86),  # F7 on beat 2 of bar 3
    (5.25, 77), (5.25, 82), (5.25, 79), (5.25, 86)   # F7 on beat 2 of bar 4
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

# Dante - Tenor Sax (motif: F, A, Bb, D, leave it hanging)
# Start on bar 2, play F, A, Bb, D over 3 beats, end on D (beat 3 of bar 2), resolve on beat 4
sax_notes = [
    (2.25, 87), (2.25, 92), (2.25, 90), (2.625, 95)  # F, A, Bb, D on beat 2 of bar 2
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
