
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
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D minor, chromatic approaches
bass_notes = [
    (1.5, 62),  # D
    (1.875, 61), # C
    (2.25, 63),  # Eb
    (2.625, 62), # D
    (3.0, 65),   # F
    (3.375, 64), # E
    (3.75, 66),  # G
    (4.125, 65), # F
    (4.5, 62),   # D
    (4.875, 61), # C
    (5.25, 63),  # Eb
    (5.625, 62)  # D
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, D7, Bm7b5, F7, Cm7
piano_notes = [
    # Bar 2
    (2.25, 67),  # D7: D, F#, A, C
    (2.25, 71),  # D7: D, F#, A, C
    (2.25, 69),  # D7: D, F#, A, C
    (2.25, 64),  # D7: D, F#, A, C
    # Bar 3
    (3.75, 65),  # Bm7b5: B, D, F, A
    (3.75, 69),  # Bm7b5: B, D, F, A
    (3.75, 67),  # Bm7b5: B, D, F, A
    (3.75, 60),  # Bm7b5: B, D, F, A
    # Bar 4
    (5.25, 67),  # F7: F, A, C, E
    (5.25, 71),  # F7: F, A, C, E
    (5.25, 69),  # F7: F, A, C, E
    (5.25, 64),  # F7: F, A, C, E
    # Bar 4
    (5.625, 57), # Cm7: C, Eb, G, Bb
    (5.625, 60), # Cm7: C, Eb, G, Bb
    (5.625, 64), # Cm7: C, Eb, G, Bb
    (5.625, 62)  # Cm7: C, Eb, G, Bb
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: Motif - D, E, F#, D (quarter notes, with a rest on the third beat)
sax_notes = [
    (1.5, 62),  # D
    (2.25, 64), # E
    (3.0, 66),  # F#
    (3.75, 62), # D
    (4.5, 62),  # D
    (5.25, 64), # E
    (6.0, 66),  # F#
    (6.75, 62)  # D
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums continue through bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
