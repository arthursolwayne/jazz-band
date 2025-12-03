
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
    # Bar 1
    (36, 0.0), (42, 0.0), (36, 0.375), (42, 0.375),
    (38, 0.75), (42, 0.75), (36, 1.125), (42, 1.125),
    (38, 1.5), (42, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (41, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (50, 1.5), (53, 1.5), (57, 1.5), (60, 1.5),
    (60, 1.75),
    (50, 2.0), (53, 2.0), (57, 2.0), (60, 2.0),
    (60, 2.25),
    (50, 2.5), (53, 2.5), (57, 2.5), (60, 2.5),
    (60, 2.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 (D-F-A-C) in Dorian mode, starting on C
sax_notes = [
    (60, 1.5), (62, 1.625), (60, 1.75), (58, 1.875),
    (60, 2.25), (62, 2.375), (60, 2.5), (58, 2.625),
    (60, 3.0), (62, 3.125), (60, 3.25), (58, 3.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Dm7 -> G7 -> Cm7
bass_notes = [
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125),
    (43, 4.5), (41, 4.875), (40, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: G7 -> Cm7
piano_notes = [
    (62, 3.0), (65, 3.0), (67, 3.0), (60, 3.0),
    (60, 3.25),
    (60, 3.5), (62, 3.5), (64, 3.5), (58, 3.5),
    (58, 3.75),
    (60, 4.0), (62, 4.0), (64, 4.0), (58, 4.0),
    (58, 4.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif variation, resolve the tension
sax_notes = [
    (62, 3.0), (60, 3.125), (58, 3.25), (60, 3.375),
    (62, 3.75), (60, 3.875), (58, 4.0), (60, 4.125),
    (62, 4.5), (60, 4.625), (58, 4.75), (60, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Cm7 -> Dm7
bass_notes = [
    (38, 4.5), (40, 4.875), (38, 5.25), (41, 5.625),
    (38, 6.0), (40, 6.375), (38, 6.75), (41, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Cm7 -> Dm7
piano_notes = [
    (58, 4.5), (60, 4.5), (64, 4.5), (58, 4.5),
    (58, 4.75),
    (50, 5.0), (53, 5.0), (57, 5.0), (60, 5.0),
    (60, 5.25),
    (50, 5.5), (53, 5.5), (57, 5.5), (60, 5.5),
    (60, 5.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Final resolution
sax_notes = [
    (60, 4.5), (62, 4.625), (60, 4.75), (58, 4.875),
    (60, 5.25), (62, 5.375), (60, 5.5), (58, 5.625),
    (60, 6.0), (62, 6.125), (60, 6.25), (58, 6.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    (36, 3.0), (42, 3.0), (36, 3.375), (42, 3.375),
    (38, 3.75), (42, 3.75), (36, 4.125), (42, 4.125),
    (38, 4.5), (42, 4.5),
    # Bar 4
    (36, 4.875), (42, 4.875), (36, 5.25), (42, 5.25),
    (38, 5.625), (42, 5.625), (36, 6.0), (42, 6.0)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
