
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
    (36, 0.0),   # Kick on 1
    (38, 0.5),   # Snare on 2
    (36, 1.0),   # Kick on 3
    (38, 1.5),   # Snare on 4
    (42, 0.0),   # Hihat on 1
    (42, 0.375), # Hihat on 2
    (42, 0.75),  # Hihat on 3
    (42, 1.125), # Hihat on 4
    (42, 1.5)    # Hihat on 5
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5),   # F
    (46, 1.875), # Gb (chromatic approach)
    (47, 2.25),  # G
    (48, 2.625), # Ab
    (48, 3.0),   # Ab
    (49, 3.375), # Bb
    (50, 3.75),  # B
    (51, 4.125), # C
    (51, 4.5),   # C
    (52, 4.875), # C#
    (53, 5.25),  # D
    (54, 5.625), # Eb
    (54, 6.0),   # Eb
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (53, 1.5),  # F
    (58, 1.5),  # A
    (57, 1.5),  # C
    (55, 1.5),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (55, 3.0),  # Bb
    (59, 3.0),  # D
    (57, 3.0),  # F
    (58, 3.0),  # Ab
    # Bar 4: F7 again (F, A, C, Eb)
    (53, 4.5),  # F
    (58, 4.5),  # A
    (57, 4.5),  # C
    (55, 4.5),  # Eb
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (36, start + 0.0),   # Kick on 1
        (38, start + 0.5),   # Snare on 2
        (36, start + 1.0),   # Kick on 3
        (38, start + 1.5),   # Snare on 4
        (42, start + 0.0),   # Hihat on 1
        (42, start + 0.375), # Hihat on 2
        (42, start + 0.75),  # Hihat on 3
        (42, start + 1.125), # Hihat on 4
        (42, start + 1.5)    # Hihat on 5
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif (F, Ab, Bb, C)
sax_notes = [
    (53, 1.5),  # F
    (55, 1.875), # Ab
    (57, 2.25),  # Bb
    (58, 2.625), # C
    (55, 3.0),   # Ab (reprise)
    (57, 3.375), # Bb (reprise)
    (58, 3.75),  # C (reprise)
    (53, 4.125), # F (resolve)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
