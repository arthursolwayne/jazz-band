
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (36, 1.5), (37, 1.75), (35, 2.0), (34, 2.25),
    (33, 2.5), (34, 2.75), (32, 3.0), (31, 3.25),
    (30, 3.5), (31, 3.75), (29, 4.0), (28, 4.25),
    (27, 4.5), (28, 4.75), (26, 5.0), (25, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (43, 2.0), (46, 2.0), (48, 2.0), (50, 2.0),  # Fm7
    (46, 3.0), (49, 3.0), (51, 3.0), (53, 3.0),  # Bb7
    (43, 4.0), (46, 4.0), (48, 4.0), (50, 4.0),  # Fm7
    (46, 5.0), (49, 5.0), (51, 5.0), (53, 5.0)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Melody in Fm, one short motif, make it sing
sax_notes = [
    # Bar 2: Start with a whisper
    (43, 1.5), (45, 1.875), (43, 2.0), (41, 2.25),
    # Bar 3: Build into a cry
    (43, 2.5), (45, 2.75), (47, 3.0), (45, 3.25),
    # Bar 4: Resolve but leave it hanging
    (43, 3.5), (45, 3.75), (43, 4.0), (41, 4.25),
    (43, 4.5), (45, 4.75), (43, 5.0), (41, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
