
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
    (0.375, 42), # Hihat on 1&
    (0.75, 38),  # Snare on 2
    (1.125, 42), # Hihat on 2&
    (1.5, 36),   # Kick on 3
    (1.875, 42), # Hihat on 3&
    (2.25, 38),  # Snare on 4
    (2.625, 42), # Hihat on 4&
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 53),  # F
    (1.75, 52), # Eb
    (2.0, 51),  # D
    (2.25, 50), # C
    (2.5, 53),  # F
    (2.75, 55), # G
    (3.0, 57),  # A
    (3.25, 55), # G
    (3.5, 53),  # F
    (3.75, 52), # Eb
    (4.0, 51),  # D
    (4.25, 50), # C
    (4.5, 53),  # F
    (4.75, 55), # G
    (5.0, 57),  # A
    (5.25, 55), # G
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4, aggressive but supportive
piano_notes = [
    (1.5, 62), # F7: F, A, C, Eb
    (1.5, 69), # Bb
    (1.5, 67), # G
    (1.5, 64), # C
    (1.5, 60), # F
    (2.25, 62), # F7: F, A, C, Eb
    (2.25, 69), # Bb
    (2.25, 67), # G
    (2.25, 64), # C
    (2.25, 60), # F
    (3.0, 62), # F7
    (3.0, 69),
    (3.0, 67),
    (3.0, 64),
    (3.0, 60),
    (3.75, 62), # F7
    (3.75, 69),
    (3.75, 67),
    (3.75, 64),
    (3.75, 60),
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    drum_notes = [
        (start + 0.0, 36),  # Kick on 1
        (start + 0.375, 42), # Hihat on 1&
        (start + 0.75, 38),  # Snare on 2
        (start + 1.125, 42), # Hihat on 2&
        (start + 1.5, 36),   # Kick on 3
        (start + 1.875, 42), # Hihat on 3&
        (start + 2.25, 38),  # Snare on 4
        (start + 2.625, 42), # Hihat on 4&
    ]
    for time, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Saxophone (Dante): One short motif, simple but emotionally charged
sax_notes = [
    (1.5, 66),  # G
    (1.75, 67), # A
    (2.0, 66),  # G
    (2.25, 64), # F
    (2.5, 66),  # G
    (2.75, 67), # A
    (3.0, 66),  # G
    (3.25, 64), # F
    (3.5, 66),  # G
    (3.75, 69), # Bb
    (4.0, 66),  # G
    (4.25, 64), # F
    (4.5, 66),  # G
    (4.75, 69), # Bb
    (5.0, 66),  # G
    (5.25, 67), # A
    (5.5, 66),  # G
    (5.75, 64), # F
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
